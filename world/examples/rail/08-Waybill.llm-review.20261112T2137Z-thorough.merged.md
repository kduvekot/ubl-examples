# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/08-Waybill.xml`, Git blob `d66e8c026ae9b2002457ba46ff93f8f963503f91` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/08#F1 · High · Road consignment note (CMR) for an international rail carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `FRC-CMR-26-0325`
- XPath: `/Waybill/cbc:Description` = `Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`
- Why: WaybillTypeCode is "The type of waybill (Bill of Laden, Airwaybill, CMR, House waybill, etc.)"; the world's list distinguishes CMR (road convention) from CIM (rail consignment note; used once over `*.xml`, `grep -rh --include='*.xml' -o 'WaybillTypeCode[^>]*>[^<]*'`). The document is typed and named as a road consignment note, and its Description ("text describing the contents of the Waybill") covers only the tractor leg to the hub. Everything else it describes is the rail main carriage: mode 2, container train FRC 4417, wagon 31 46 4521 042-3, across the Urvania–Bayvarra border to Lumeway's siding in Marrowdale, with rail freight and electric-traction emissions. The road leg itself has no stage. Refutation tried in the merge: CMR art. 2 extends the road convention to a road vehicle carried on another mode, but here containers, not road vehicles, travel by train, so it does not apply (own knowledge). The type contradicts the mode and content of the same document.
- Condition: WaybillTypeCode, Name, Description and the carrier's reference name a consignment note for the carriage the stages describe (rail main carriage; the road leg, if covered, as pre-carriage), or the waybill documents only the road leg and then carries no rail stage and no delivery in Bayvarra.
- Options: (a) preferred: CIM (or a world code for the Trade Accord's rail consignment note), with matching name and carrier reference, a description of the consignment and carriage, and the carrier haulage as a PreCarriageShipmentStage (mode 3); (b) two documents: a CMR for the haulage and a rail note for the main carriage (adds a document to the flow).
- Needs decision: yes (which convention governs the carriage is part of the story; option (b) adds a document; broad and logistics yes, context no)
- From: broad (F1), logistics (F1), context (F1, F9)

### rail/08#F2 · High · Shipment gross weight leaves out the containers its definition includes
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". Recalculated in the merge: 2 × 7884 = 15 768 kg for the two loaded containers; goods 7968 / 2 = 3984 kg per box, tare 3900 kg each, a normal tare for a 40-foot high cube. 7968 kg is the goods with packing only (the consignments of 02 and 03, the goods item of 06). The transit declaration has the same value (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`).
- Condition: Shipment/GrossWeightMeasure = goods plus packaging plus equipment (15 768 kg), or it is absent and the goods weight is given on the consignment.
- Options: (a) preferred: 15 768 kg, and 7968 kg as Consignment/GrossWeightMeasure as in 02 and 03; (b) remove the shipment weight.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### rail/08#F3 · High · An actual waypoint after the waybill was issued
- XPath: `/Waybill/cbc:IssueTime` = `13:10:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- Why: ActualWaypointTransportEvent is "The location of an actual waypoint during a transportation service". The waybill, issued on 14 April at 13:10, records the train actually passing its waypoint at 13:20 the same day, ten minutes after issue. Both times are local to the same document (no time zone between them), so the contradiction holds.
- Condition: Every actual event lies at or before the issue time; later events are planned or estimated.
- Options: (a) preferred: drop the actual waypoint (a consignment note records the takeover, not the progress of the journey) and keep the planned one; (b) issue the waybill later, if the world's waybill is updated en route (then F5 and the timeline need checking too).
- Needs decision: no
- From: broad (F3), logistics (F3)

### rail/08#F4 · High · Customs as issuer of the declaration that Valdara made
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: CustomsDeclaration/IssuerParty is "The Party who issues this Customs Declaration". VI-TD-26-0331 is the transit declaration 06, whose ID ("assigned by the sender") is in Valdara's series; Valdara makes it as TransitExporterParty ("The Party who makes the Transit Customs Declaration, or on whose behalf…") and signs it (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`); the customs administration processes it (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`). Refutation tried: customs would be the issuer of a customs-assigned number (e.g. a movement reference number), but the ID quoted is the declarant's own document number. The waybill contradicts the referenced example.
- Condition: The issuer of the referenced declaration in both handling units is the party that issued 06 (Valdara Industries, `XU-R-104274`), or the reference is a customs-assigned number that 06 also carries.
- Options: (a) preferred: Valdara Industries as IssuerParty; (b) quote a customs-assigned reference (added to 06's story) and keep customs as its issuer; (c) drop IssuerParty.
- Needs decision: no
- From: parties (F1), broad (F5, issuer part), context (F4)

### rail/08#F5 · High · The waybill cites a customs declaration issued four hours after it
- XPath: `/Waybill/cbc:IssueTime` = `13:10:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cbc:IssueTime` = `17:29:00`
- Why: The reference resolves to the transit declaration 06, but that declaration is issued on the same day at 17:29, four hours after this waybill (13:10) and ten hours after the train left (06:52). A document cannot cite the number of a declaration that does not exist yet, so the reference is broken as it stands (section 6, High). Broad included this in its High issuer finding, logistics made it Medium; parties and context noted it as a timeline question. It is kept as a finding because it is a contradiction between this example and the example it refers to; which of the two times is wrong (transit has to be declared before departure) is part of the decision.
- Condition: The customs declaration the waybill references exists at the waybill's issue time.
- Options: (a) preferred: the transit declaration is issued before departure (e.g. 13 April evening, after the loading proof), which fixes the reference and the transit timeline together; (b) remove the reference from the waybill.
- Needs decision: yes (changes the flow's timeline)
- From: logistics (F6), broad (F5, timing part); parties and context listed it under "Outside this review"

### rail/08#F6 · High · Distribution of the originals contradicts the note and its own distribution type
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: DocumentDistribution/Party is "The interested Party who receives this Document". The note says there are three originals, for consignor, consignee and carrier. The list gives "the consignee's original" to Ferrano Intermodal Hub, the terminal at the start of the rail stage, not the consignee (Lumeway Distribution, Marrowdale): the party contradicts the distribution type next to it. The consignor, which by the note receives an original, is listed for an electronic copy only, and the carrier's original is not listed. Refutation tried: "with the goods" explains why the hub may hold the paper on the way, but not why the hub is the interested party receiving the consignee's original; a list that omits the carrier's own copy would be incompleteness, but the hub/consignee and original/copy mismatches are contradictions.
- Condition: The distribution list and the note describe the same originals and recipients: the consignee's original to the consignee (travelling with the goods), the consignor's original to the consignor, the carrier's kept by the carrier, copies in addition; or the note says what is distributed.
- Options: (a) preferred: three distributions (original to Valdara, original with the goods for Lumeway, original kept by Ferrano Rail Cargo); (b) change the note if the world's procedure differs.
- Needs decision: no (parties said yes; the preferred fix is encoding)
- From: broad (F4), parties (F7), context (F5)

### rail/08#F7 · Medium · Consignment ID used as shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0327`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". VI-CS-26-0327 is the consignment's ID, not an order or instruction; no document of the flow has this ID. The transport user's instruction is the request VI-TR-26-0326 (02), confirmed by the plan 03, which the waybill references. Same misuse in 07.
- Condition: ShippingOrderID is absent or holds the ID of the shipping order or forwarding instruction for this shipment.
- Options: (a) preferred: VI-TR-26-0326 (broad, logistics); (b) remove it, since the plan is referenced.
- Needs decision: no
- From: broad (F7), logistics (F4)

### rail/08#F8 · Medium · The wagon given as equipment contained in the container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:ID` = `31 46 4521 042-3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:TransportEquipmentTypeCode` = `RR`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ApplicableTransportMeans/cac:RailTransport/cbc:RailCarID` = `31 46 4521 042-3`
- Why: UBL defines ContainedInTransportEquipment as "A piece of transport equipment contained in this piece of transport equipment". By that definition the waybill says the rail car (RR) is inside container FRXU1044175; it is the other way round. The element's name suggests the reverse relation, so name and definition disagree in UBL itself; under semantic conformance (CLAUDE.md) the definition governs, which is why the merge does not need a decision here. The wagon is already identified correctly as RailCarID and in StowagePositionID; the second container has no such relation.
- Condition: No equipment is stated to be contained in a piece of equipment it is not inside.
- Options: (a) preferred: remove ContainedInTransportEquipment and record the name/definition conflict as a finding for the TC write-up; (b) describe the wagon as equipment of its own, if a direct relation is wanted.
- Needs decision: no (logistics said yes, if the owner reads the element by its name; the agreed rule of semantic conformance settles that)
- From: logistics (F5), context (F3)

### rail/08#F9 · Medium · EmissionCalculationLocation names an office, not a geographic context
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionCalculationLocation/cbc:Name` = `Ferrano Rail Cargo, energy office`
- Why: EmissionCalculationLocation is "The geographical context in which this environmental emission was calculated or for which the emission factor applies, such as the country of a national database or regulatory regime". The value is the carrier's department that did the calculation. The factor implied, 410 kg / (2 × 610 kWh) = 0.336 kg CO2e per kWh (recalculated in the merge), is a grid factor of a country or market, which is what the element should name.
- Condition: The location names the geographic area of the factor (e.g. the country or electricity market, with its code), or is absent.
- Options: (a) preferred: the country (Urvania, or the Trade Accord grid if the train runs on both grids) as Location with Address/Country; (b) drop it.
- Needs decision: no
- From: broad (F8), logistics (F9), parties (F6), context (F18)

### rail/08#F10 · Medium · Container "being stored" at the hub while it is on the train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:StorageLocation/cbc:Name` = `Ferrano Intermodal Hub, stack C`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DispositionCode` = `LOADED`
- Why: StorageLocation is "The location where this piece of transport equipment is being stored". At 13:10 the container is loaded (DispositionCode LOADED, loading 05:40) on a train that left at 06:52; it is no longer stored in stack C, where it waited after the handling at 18:30 on 13 April. The element carries a past storage, not the one its definition names. Medium (broad) rather than High: the value can be read as the storage the box had at the hub, so it is a misuse rather than a hard contradiction; logistics and context said Low.
- Condition: StorageLocation is absent, or states where the equipment is stored at the time of the document.
- Options: (a) preferred: move "stack C" to the HandlingTransportEvent's location (context); (b) drop it.
- Needs decision: no
- From: broad (F6), logistics (F13, storage part), context (F15)

### rail/08#F11 · Medium · Waypoints without a location
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedWaypointTransportEvent/cbc:OccurrenceTime` = `13:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- Why: A waypoint is a place passed ("The location of an actual waypoint during a transportation service"; "A waypoint planned by the party providing a transportation service"). Neither event has a location, so they say only that the train is somewhere at 13:00/13:20. The request names the waypoint (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`). The event's meaning depends on the place, hence Medium (logistics, context; broad Low).
- Condition: Every waypoint event carries its location.
- Options: (a) preferred: Location = the rail border station (name and, if the world has one, an identifier) on the planned waypoint; the actual one is handled by F3.
- Needs decision: no
- From: logistics (F8), context (F6), broad (F12)

### rail/08#F12 · Medium · Province given in Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity), as the consignee's address in the same document uses (`/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files.
- Condition: No Urvanian address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad, context yes; aligned with rail 01–05, wood, plastics)
- From: broad (F9), parties (F2), context (F8)

### rail/08#F13 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is a language and repeats `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`. 364 occurrences in 213 example files.
- Condition: LocaleCode is absent or names a locale from a list of locales.
- Options: (a) preferred: drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F10), parties (F3), context (F7)

### rail/08#F14 · Medium · A gate in AdditionalStreetName of the consignee's postal address
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street. The waybill delivers by rail to the siding (`/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Rail siding of Lumeway Distribution, Marrowdale`), so the road gate is neither part of the address nor the delivery point.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) preferred: remove it; (b) where a gate matters, state it at the delivery location.
- Needs decision: no
- From: broad (F11), parties (F4)

### rail/08#F15 · Low · Terminal named as operator of a carrier-owned container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OperatingParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OwnerParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:OwnerTypeCode` = `CARRIER`
- Why: OperatingParty is "The Party who operates this piece of Transport Equipment". Parties (Medium): the operator of a container is the party that controls its use and deployment (own knowledge: "container operator"), here the carrier, which owns and provides the box, sends it to the warehouse and orders its empty return; storing and lifting at the hub are terminal services; the second container has no operating party at all. Broad and logistics refuted it: a terminal can operate the carrier's box pool on its site ("operates" for the terminal part), and nothing in the flow contradicts it. The definition is too short to settle either reading, so the merge keeps it as Low with both arguments.
- Condition: The operating party, if given, is the party the world means by "operates" for this container, the same for both containers.
- Options: (a) preferred: drop OperatingParty (owner and provider already name the carrier); (b) Ferrano Rail Cargo as operator; (c) show the hub's role through a handling or storage event with the hub as location.
- Needs decision: yes (cannot be settled)
- From: parties (F5); broad and logistics listed it under "Considered and refuted"

### rail/08#F16 · Low · 96 assembled benches per container do not fit the stated container volume
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:SummaryDescription` = `192 park benches in two 40-foot containers.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossVolumeMeasure` = `76.3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`
- XPath: `06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: Physics redone in the merge, with the bench dimensions of 06 (1800 × 620 × 780 mm). Bounding volume 0.870 m³; 96 per box = 83.6 m³ > the stated 76.3 m³ (the internal volume of a 40-foot high cube, about 12.03 × 2.35 × 2.70 m). Whole boxes fit 54 upright (6 × 3 × 3) or at best 72 on their backs (6 × 3 × 4). If 76.3 m³ were read as an external volume the space would be even smaller (logistics' note under "Considered and refuted"). Weight is no limit: 3984 kg of goods per box against a payload of about 26.5 t. 96 per box fits only knocked down or nested, which no document says. Lowered from logistics' Medium to Low, as in 06: the contradiction rests on an unstated assumption (assembled benches), and cast-frame benches are commonly shipped knocked down; broad listed the capacity question under "Outside this review" and made it a finding in 06.
- Condition: The number of benches per container is possible for the way they are packed, and the packing follows from the documents.
- Options: (a) preferred: state that the benches travel knocked down (about 0.25 m³ each), in the goods description or as packages; (b) about 54 per container, i.e. four containers or fewer benches (changes the order and invoices).
- Needs decision: yes
- From: logistics (F7); broad ("Outside this review")

### rail/08#F17 · Low · Freight charge stated for only one of the two containers
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Rail freight per container`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`
- XPath: `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `109200`
- Why: TransportEquipment/FreightAllowanceCharge is "A freight allowance charge associated with this piece of transport equipment". FRXU1044175 carries the rail freight of 54 600 XUF "per container"; FRXU1044180, equal in type, load and weight on the same train, carries none. The waybill thus shows 54 600 XUF of freight, while the freight invoice that references it bills 2 × 54 600 = 109 200 XUF. Low: the waybill states no total, so it is incomplete rather than contradictory.
- Condition: Both containers carry their freight charge, or the waybill states the freight once for both; the freight in the waybill adds up to what 10 bills.
- Options: (a) preferred: the same FreightAllowanceCharge on the second container; (b) the freight once for the consignment (109 200 XUF).
- Needs decision: no
- From: money (F1), broad (F13, charge part)

### rail/08#F18 · Low · The second container lacks the wagon, places and events the first has
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:SizeTypeCode` = `45G1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:StowagePositionID` = `31 46 4521 042-3 / A`
- Why: For FRXU1044175 the waybill gives the wagon and slot (A), the train, loading and unloading places, pickup, handling, loading and delivery events, owner, provider. For FRXU1044180, carried under the same note on the same train, it gives none, so the note does not say on which wagon or slot the second box travels, nor where it is loaded or delivered.
- Condition: Both containers carry their wagon/stowage position and at least loading and unloading locations, or what both share is stated once at consignment or stage level.
- Options: (a) preferred: give the second container its wagon (e.g. slot B) and the same places; (b) move shared data (places, delivery) to the consignment or stage.
- Needs decision: no
- From: logistics (F15), broad (F13, equipment part)

### rail/08#F19 · Low · Stale estimated departure next to the actual departure
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- Why: Issued at 13:10, after the actual departure at 06:52, the waybill still carries an estimate of 06:50 that the actual time in the same stage supersedes.
- Condition: No estimate for an event whose actual time the document reports.
- Options: (a) preferred: drop the estimated departure; (b) issue the waybill at takeover, before departure (see F3, F5).
- Needs decision: no
- From: context (F14), logistics (F13, estimate part)

### rail/08#F20 · Low · Issue location and other places named after companies
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:MeasurementFromLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: IssueLocation is "The location where this waybill was issued"; the value is a company, while the same document names the place "Castrano Logistics warehouse, Ferrano", and 02/03 name it "Castrano Logistics" with a street address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`). The hub appears only by the operator's name, while the same document identifies other places properly (LoadingLocation XUFER, the siding's GLN). Logistics adds that issuing at the warehouse at 13:10 on 14 April, 22 hours after the pickup there, does not fit a note made out at takeover (part of the timeline, see "Outside this review").
- Condition: Each place (warehouse, terminal) has one name that names the place, the same in every example of the flow, and an identifier where the flow has one; the issue location is the place where the carrier issues the note.
- Options: (a) preferred: one place name per location plus an identifier (GLN or similar); issue location "Castrano Logistics warehouse, Ferrano" with an issue time at takeover, or the carrier's office if the time stays; (b) at least the warehouse's address.
- Needs decision: no
- From: broad (F14, issue-location part), logistics (F10), parties (F9), context (F10)

### rail/08#F21 · Low · The equipment references the waybill itself
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ShipmentDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- XPath: `/Waybill/cbc:ID` = `FRC-WB-26-0334`
- Why: ShipmentDocumentReference is "A reference to a shipping document associated with this piece of transport equipment". The document referenced is the waybill in which it stands; it adds nothing (IND5/IND6), and the second container has none.
- Condition: The reference points to another document, or is absent.
- Options: (a) preferred: drop it; (b) a document of its own for the container (e.g. an equipment interchange receipt), if the world has one.
- Needs decision: no
- From: broad (F14, self-reference part), logistics (F14), context (F17)

### rail/08#F22 · Low · Passenger quantity 0 on a freight train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: PassengerQuantity is "The total number of passengers aboard a transport means"; a container train carries none by its nature, and stating 0 has no business reason (IND5/IND6). Same in the plan 03.
- Condition: PassengerQuantity is absent unless the story gives a reason.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F14, filler part), logistics (F12), context (F13)

### rail/08#F23 · Low · Performing carrier repeats the contracted carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:PerformingCarrierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104685`
- XPath: `/Waybill/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104685`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:PerformingCarrierAssignedID` = `FRC-J-26-3318`
- Why: PerformingCarrierParty is "The Party who performs the carriage of this Consignment"; next to the carrier it has a reason when another carrier performs (part of) the carriage. Here both are Ferrano Rail Cargo, also beyond the border, so the element and its assigned ID repeat the carrier (section 4.8).
- Condition: Performing-carrier data is present only when a different carrier performs (all or part of) the carriage.
- Options: (a) preferred: drop PerformingCarrierParty and PerformingCarrierAssignedID (parties would keep the journey reference); (b) a different performing carrier beyond the border, which changes the story.
- Needs decision: no
- From: parties (F13), context (F12)

### rail/08#F24 · Low · Demurrage instructions for containers at a siding, under a definition about vessels
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions` = `Free time five days at the siding, then demurrage per container day.`
- Why: DemurrageInstructions is "Text of instructions relating to demurrage (the case in which a vessel is prevented from loading or discharging cargo within the stipulated laytime)". The value is container free time at a rail siding. Whether the parenthesis restricts the element to vessels decides whether this is a misuse; the same text is in the plan 03.
- Condition: The owner confirms the parenthesis is only an example (recorded as a UBL definition question), or the free time is stated elsewhere (e.g. the equipment's Information).
- Options: (a) preferred: keep and record the definition question (container and wagon demurrage are established rail practice); (b) move the text.
- Needs decision: yes
- From: logistics (F11)

### rail/08#F25 · Low · Container "not under the Container Convention" while travelling under customs seal
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:LegalStatusIndicator` = `false`
- Why: LegalStatusIndicator is "An indication of the legal status of this piece of transport equipment with respect to the Container Convention Code". The containers cross a border under transit with seals that "remain intact" (06); containers approved for transport under customs seal carry that status (own knowledge: Customs Convention on Containers). "false" is at odds with that, unless the story explains it; the indicator's meaning is imprecise in UBL, so it may also simply be a filler.
- Condition: The indicator is absent, or true for a container used under customs seal, or the story explains why it is not approved.
- Options: (a) preferred: drop it; (b) true.
- Needs decision: yes
- From: context (F16)

### rail/08#F26 · Low · Contacts do not fit the roles
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the waybill as consignor; questions about the note go to its shipping function, not the order desk. A consignee's contact receives goods; the waybill asks to "Deliver against signature of the consignee" (`/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`), so the carrier needs Lumeway's goods-in or siding contact, not its sales customer service.
- Condition: Role-specific contacts (consignor's shipping, consignee's goods receiving), or none.
- Options: (a) preferred: role-specific contacts; (b) drop Contact where it does not fit.
- Needs decision: no
- From: broad (F15), parties (F10, F11)

### rail/08#F27 · Low · Legal-entity master data the waybill does nothing with
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: A waybill does nothing with the consignor's stock-exchange listing or the share capital of consignor and consignee (section 4.8). (Valdara's ServiceProviderParty Castrano Logistics is used: it is the loading-proof party and the pickup place; see "Considered and refuted".)
- Condition: Every legal-entity element present has a purpose in the waybill.
- Options: (a) preferred: drop SecurityListing and CorporateStockAmount here; (b) a reduced party description for transport documents.
- Needs decision: no
- From: parties (F12), context (F11)

### rail/08#F28 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5); these are tagged `en-XU` but are Italian (own knowledge). A world convention for street names cannot be ruled out; the legal forms are the stronger case. 217 such renderings in 102 example files.
- Condition: Every rendering tagged as English is English, or the world records the Italianate English usage.
- Options: (a) record the convention (preferred if intended); (b) translate; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F8)

### rail/08#F29 · Low · Carrier's registration date 1996-01-01
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Not raised by any part of this run; added by the merge for consistency with rail 01–05 and earlier flows (271 occurrences in 181 example files): the date reads as a default, unless a 1996 (re-)registration is part of the story.
- Condition: Each company's registration date is its own, or the world records a general 1996 registration.
- Options: (a) preferred: own date per company; (b) record a 1996 re-registration in the story.
- Needs decision: yes
- From: merge

## Checked and consistent
- References: `FRC-TEP-26-0328` resolves to 03; consignment, shipment, containers, seals, weights and the contract FRC-CON-2026-005 agree with 03 and 06; ContractedCarrierAssignedID `FRC-CON-2026-005/88` agrees with the plan's call-off 88; the waybill is referenced by the freight invoice (`10-Invoice.xml:/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`), whose price 54 600 XUF per slot equals the charge per container.
- Rail stage times: planned 06:45/10:30, estimated 06:50/10:40, actual departure 06:52 equal 03 and 05; equipment events in order: positioning 12 April 08:00, pickup 13 April 15:00, handling 18:30, loading 14 April 05:40, despatch 06:50, delivery planned 15 April 11:00 (= 03, 07), latest delivery 16 April (= 02, 03). Train FRC 4417, journey CT 4471, mode 2, means type 2302, direction WB, loading sequence 7, crew 2: as in 03.
- Loading location Ferrano (XUFER) and unloading location Marrowdale (XBMRW) agree with the stage's instructions and the delivery location; XU/XB are user-assigned ISO 3166 codes, so the LOCODEs cannot be mistaken for real ones.
- Weights and equipment (merge recalculation): 7884 kg per loaded box = 3984 kg goods + 3900 kg tare; 45G1 = 40 ft high cube, length 12 192 mm, internal volume 76.3 m³ plausible; owner and provider Ferrano Rail Cargo agree with ProviderTypeCode/OwnerTypeCode CARRIER and with the return to the hub within five days (= the free time).
- Energy and emission (merge recalculation): 2 × 610 kWh = 1220 kWh; 410 / 1220 = 0.336 kg CO2e per kWh, a plausible grid factor (own knowledge). Logistics' order-of-magnitude check (about 0.02 kWh per gross tonne-km for electric freight, about 19 t per slot) fits a long journey of about 28 h.
- Money: PrepaidPaymentTerms "Freight prepaid by the consignor under DAP." agrees with 03, with DAP in 01 and with the freight invoice to Valdara; AdValoremIndicator false fits freight charged per container; reason code FC ("Freight service") fits.
- Check digits (from the parts): containers FRXU1044175 and FRXU1044180 (ISO 6346), GLN 9520610900015 and 9520610900008, ISIN pass check_ids.py; the wagon number 31 46 4521 042-3 passes the UIC (Luhn) self-check digit (parts' calculation: digit sum 47, check digit 3). Whether owner code FRXU and UIC country code 46 are assigned in the real registers was not checked.
- Parties: sender, carrier and signatory Ferrano Rail Cargo; receiver and consignor Valdara; consignee Lumeway; loading proof party Castrano Logistics (`XU-R-104411`), the warehousing provider of Valdara and the pickup place: same identifiers and descriptions as in the other rail examples.

## Considered and refuted
- `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`: copied master data — refuted because Castrano loads the containers (LoadingProofParty) and the boxes are picked up at its warehouse, so the waybill uses it. (from broad, parties, context)
- `/Waybill/cbc:CarrierAssignedID` = `FRC-CMR-26-0325`: duplicate of the waybill number — refuted because a carrier may keep its own reference next to the document number; its "CMR" follows the typing of F1, where it is cited. (from broad)
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossVolumeMeasure` = `76.3`: possibly the external volume (12.192 × 2.438 × 2.896 m ≈ 86.1 m³) — not settled, but either reading leaves F16 standing. (from logistics)
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DamageRemarks` = `Small dent in the left side panel, noted at pick-up; no effect on the cargo.`: damage noted at pick-up in a later document — refuted: the remark states when it was noted. (from logistics)
- `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Valdara Industries`: consignor without address — refuted: the same party (same ID) is the receiver with its full address. (from parties)
- `/Waybill/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`: a consignment note is signed by sender and carrier — refuted: UBL's Signature is the electronic document's signature by its issuer. (from parties)
- `/Waybill/cac:Shipment/cac:Consignment/cbc:ContractedCarrierAssignedID` = `FRC-CON-2026-005/88`: contract number used as consignment ID — refuted: the call-off number under the framework contract is how the contracted carrier identifies the consignment. (from context)
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:PowerIndicator` = `false`: filler — refuted: it states a property of the equipment (a dry box has no power supply), not implied by absence. (from context)
- `/Waybill/cbc:AdValoremIndicator` = `false`: filler — refuted: it states that no ad valorem freight applies, which a waybill legitimately says. (from context, money)
- `/Waybill/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms`: "prepaid" although the freight is invoiced later with 30 days to pay — refuted: "prepaid" is the freight term (borne by the consignor), not a payment in advance. (from money)
- The OperatingParty refutations of broad and logistics are carried into F15, where the parties' finding stays as Low with both arguments.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 + context/F9 → F1: combined (the Description is evidence of the same typing problem); needs decision yes (context no); refutation via CMR art. 2 added.
- broad/F5 split: issuer part → F4 (with parties/F1 High, context/F4 Medium; kept High: contradiction with 06); timing part → F5 (with logistics/F6 Medium/yes), raised to High as a reference to a document not yet issued; needs decision yes.
- broad/F4 (High), parties/F7 (Medium, yes), context/F5 (Medium) → F6: High, because the party contradicts its own distribution type and the note; needs decision no.
- broad/F6 (Medium), logistics/F13 storage part (Low), context/F15 (Low) → F10: Medium.
- logistics/F13 estimate part, context/F14 → F19: separated from the storage finding (different element and fix).
- broad/F12 (Low), logistics/F8, context/F6 (Medium) → F11: Medium.
- logistics/F5 (yes), context/F3 (no) → F8: needs decision no (semantic conformance settles the reading).
- broad/F8, logistics/F9, parties/F6 (Medium), context/F18 (Low) → F9: Medium; factor recalculated.
- parties/F5 (Medium) → F15: lowered to Low, needs decision yes, because broad and logistics refuted it and the merge could not settle it.
- logistics/F7 (Medium) → F16: lowered to Low, aligned with 06 (unstated packing assumption); physics redone.
- broad/F13 split: charge part → F17 (with money/F1), equipment part → F18 (with logistics/F15).
- broad/F14 split into F20 (issue location, with logistics/F10, parties/F9, context/F10), F21 (self-reference, with logistics/F14, context/F17) and F22 (PassengerQuantity, with logistics/F12, context/F13).
- broad/F9, parties/F2, context/F8 → F12: needs decision no (broad, context yes).
- broad/F10, parties/F3, context/F7 → F13; broad/F11, parties/F4 → F14; broad/F15, parties/F10, F11 → F26; parties/F12, context/F11 → F27; parties/F13, context/F12 → F23: combined.
- parties/F8 → F28: count replaced by 217 in 102 files.
- F29 added by the merge (registration date 1996-01-01).

## Outside this review
- Timeline: the waybill is issued at 13:10 on 14 April, a day after the boxes were collected at the warehouse (13 April 15:00) and six hours after the train left (06:52); a consignment note is normally made out when the carrier takes over the goods. The transit declaration it cites is issued later still (F5). (from broad, logistics, parties, context)
