# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/08-Waybill.xml`, Git blob `d66e8c026ae9b2002457ba46ff93f8f963503f91` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/08#F1 · High · A road consignment note (CMR) for an international rail carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`
- Why: The waybill's type and name say it is a consignment note under the road convention (CMR), and its description is the road leg ("the rail carrier's tractor brings the packed boxes to the hub"). Everything the document actually describes is the rail carriage: main carriage by mode 2 (rail) on train FRC 4417 from the Ferrano hub to Marrowdale across the Urvania–Bayvarra border, wagon 31 46 4521 042-3, emissions from the hub to Marrowdale, delivery at the Lumeway siding. An international rail carriage is documented by a rail consignment note (own knowledge: CIM consignment note under COTIF, or a regional equivalent), and the CMR covers road carriage only. The road leg itself has no stage in this waybill. The type code thus contradicts the transport mode and the content of the same document.
- Condition: WaybillTypeCode and Name name a consignment note for the mode of the carriage the waybill describes, and that carriage is the one its stages describe (rail main carriage; the road leg, if covered, as pre-carriage).
- Options: (a) preferred: a rail consignment note type (e.g. a world code for the Trade Accord's rail consignment note, or CIM) with matching name, the description saying what the note covers, and the carrier-haulage road leg as a `cac:PreCarriageShipmentStage` (mode 3); (b) keep a CMR for the road leg only and move the rail carriage to a second waybill (adds a document to the flow).
- Needs decision: yes

### rail/08#F2 · High · Shipment gross weight leaves out the containers
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment GrossWeightMeasure is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The goods with packaging weigh 7968 kg (rail/02, rail/03, rail/06 goods item); the two loaded containers weigh 2 × 7884 = 15 768 kg (each 3984 kg goods + 3900 kg tare). The shipment's gross weight must be 15 768 kg. The transit declaration has the same value for the same shipment (rail/06#F1).
- Condition: Shipment GrossWeightMeasure equals goods plus packaging plus equipment (15 768 kg), or it is absent and the goods weight is given on the consignment.
- Options: (a) preferred: 15 768 kg, and the goods weight 7968 kg as `cac:Consignment/cbc:GrossWeightMeasure` as in rail/02 and rail/03; (b) remove the shipment weight.
- Needs decision: no

### rail/08#F3 · High · An "actual" waypoint after the waybill was issued
- XPath: `/Waybill/cbc:IssueTime` = `13:10:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- Why: The waybill is issued on 2026-04-14 at 13:10 and records an actual waypoint at 13:20 the same day, ten minutes later. An actual event cannot lie after the issue of the document that reports it.
- Condition: Every actual event lies at or before the issue time; events after it are planned or estimated.
- Options: (a) preferred: remove the actual waypoint (a consignment note records the takeover, not the progress of the journey) and keep the planned waypoint; (b) issue the waybill later — but then F6 and the cross-document timeline need to be checked as well.
- Needs decision: no

### rail/08#F4 · Medium · The consignment ID is given as the shipping order
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0327`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: Waybill ShippingOrderID is "an identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". VI-CS-26-0327 is the consignment's ID, not an order or instruction; no document of the flow has this ID. The transport user's instruction in this flow is the request rail/02 (VI-TR-26-0326), confirmed by the plan rail/03, which this waybill references in DocumentReference. The same misuse is in rail/07.
- Condition: ShippingOrderID is absent or holds the ID of the shipping order or forwarding instruction for this shipment.
- Options: (a) preferred: VI-TR-26-0326; (b) remove it, since the plan is referenced.
- Needs decision: no

### rail/08#F5 · Medium · The wagon is given as equipment contained in the container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:ID` = `31 46 4521 042-3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:TransportEquipmentTypeCode` = `RR`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ApplicableTransportMeans/cac:RailTransport/cbc:RailCarID` = `31 46 4521 042-3`
- Why: UBL defines ContainedInTransportEquipment as "a piece of transport equipment contained in this piece of transport equipment". By that definition the waybill says the rail car (RR) is inside the container FRXU1044175; it is the other way round, the container stands on the wagon. The element's name ("contained in") suggests the reverse relation, so name and definition disagree in UBL itself; under the rule of semantic conformance the definition governs. The wagon is already identified correctly as the container's ApplicableTransportMeans (RailCarID) and in the stowage position.
- Condition: No transport equipment is stated to be contained in a piece of equipment it is not inside; the wagon is identified only where its relation to the container is the right one.
- Options: (a) preferred: remove ContainedInTransportEquipment (RailCarID and StowagePositionID already carry the wagon) and record the name/definition conflict as a finding for the UBL TC; (b) if the owner reads the element by its name, record that decision explicitly.
- Needs decision: yes

### rail/08#F6 · Medium · The waybill lists a customs declaration issued four hours after it
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `/Waybill/cbc:IssueTime` = `13:10:00`
- Why: The reference resolves to the transit declaration rail/06, but that declaration is issued on 2026-04-14 at 17:29 (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cbc:IssueTime` = `17:29:00`), four hours after this waybill (13:10) and ten hours after the train left (06:52). A document cannot cite the number of a declaration that does not exist yet. Which of the two times is wrong (the transit declaration should precede departure) is a timeline question for the cross-document review; the reference itself is broken as it stands.
- Condition: The customs declaration the waybill references exists at the waybill's issue time.
- Options: (a) preferred: the transit declaration is issued before the departure (e.g. 2026-04-13 evening, after loading proof), which fixes the reference and the transit timeline at once; (b) remove the reference from the waybill.
- Needs decision: yes

### rail/08#F7 · Medium · 96 benches per container do not fit by volume
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:SummaryDescription` = `192 park benches in two 40-foot containers.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossVolumeMeasure` = `76.3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`
- Why: Calculated: a bench measures 1800 × 620 × 780 mm (the item dimensions in `06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`, and Dimension[2] 620, Dimension[3] 780), a bounding volume of 0.870 m³; 96 benches per container (192 / 2) need 83.6 m³, more than the container's stated 76.3 m³ (the internal volume of a 40-foot high cube). Stacked as rigid boxes in the internal space 12.03 × 2.35 × 2.70 m (own knowledge), at most 54–57 assembled benches fit (e.g. 6 along × 3 across × 3 high = 54; on end 19 × 3 = 57). 96 benches fit only knocked down or nested, which no document says (the order's packaging waste "stretch film and pallet straps, per bench" suggests wrapped benches on pallets). Weight is no limit: 3984 kg of goods per box.
- Condition: The number of benches per container is possible for the way they are packed, and the packing (assembled, knocked down, nested, palletised) follows from the documents.
- Options: (a) preferred: state that the benches are shipped knocked down (frames and slats separate) in the goods description or as packages, which makes 96 per box plausible (about 0.25 m³ each); (b) reduce to about 54 benches per container, i.e. four containers or fewer benches (changes the order and invoices).
- Needs decision: yes

### rail/08#F8 · Medium · Waypoints without a location
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedWaypointTransportEvent/cbc:OccurrenceTime` = `13:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- Why: ActualWaypointTransportEvent is defined as "the location of an actual waypoint during a transportation service", PlannedWaypointTransportEvent "a waypoint planned by the party providing a transportation service"; a waypoint is a place passed. Neither event has a location, so the waybill says nothing about where the train is planned to be at 13:00. The request names the waypoint (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`).
- Condition: Every waypoint event carries its location.
- Options: add `cac:Location` with the border station (name and, if the world has one, a UN/LOCODE) to the planned waypoint; the actual one is handled by F3 (preferred).
- Needs decision: no

### rail/08#F9 · Medium · The emission calculation location is an office, not a geographical context
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionCalculationLocation/cbc:Name` = `Ferrano Rail Cargo, energy office`
- Why: EmissionCalculationLocation is "the geographical context in which this environmental emission was calculated or for which the emission factor applies, such as the country of a national database or regulatory regime". The value is the carrier's department that did the calculation, not a geographical context. The emission factor implied here, 410 kg / (2 × 610 kWh) = 0.336 kg CO2e per kWh, is a grid factor of a country or market, which is what the element should name.
- Condition: EmissionCalculationLocation names the geographical context of the factor (e.g. the country or electricity market whose grid factor is used), or is absent.
- Options: (a) preferred: the country (Urvania, or the Trade Accord's electricity market if the train runs on both grids), as a Location with Address/Country; (b) remove it.
- Needs decision: no

### rail/08#F10 · Low · Issue location named after a company, and the note issued at the warehouse a day after pickup
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cbc:ActualPickupDate` = `2026-04-13`
- XPath: `/Waybill/cbc:IssueDate` = `2026-04-14`
- Why: IssueLocation is "the location where this waybill was issued"; the value is a company, not a place (the same place is named "Castrano Logistics warehouse, Ferrano" in the pickup location of this waybill). It also says the note was issued at the warehouse, while the issue time is 2026-04-14 13:10, about 22 hours after the containers were picked up there (2026-04-13 15:00) and six hours after the train left the hub. A consignment note is made out at the takeover of the goods.
- Condition: The issue location is a place, and the place and time of issue fit each other (the warehouse at takeover, or the carrier's office at the later time).
- Options: (a) preferred: issue location "Castrano Logistics warehouse, Ferrano" and an issue time at the takeover on 2026-04-13 (which also resolves F3); (b) keep the time and name the carrier's office in Ferrano as the issue location.
- Needs decision: no

### rail/08#F11 · Low · Demurrage instructions for containers at a siding, under a definition about vessels
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions` = `Free time five days at the siding, then demurrage per container day.`
- Why: DemurrageInstructions is "text of instructions relating to demurrage (the case in which a vessel is prevented from loading or discharging cargo within the stipulated laytime)". The value is container free time at a rail siding. Whether the parenthesis restricts the element to vessels decides whether this is a misuse; the same is in the plan (rail/03#F10).
- Condition: The owner confirms the parenthesis is only an example (recorded as a UBL definition question), or the free time is stated elsewhere (e.g. the equipment's Information).
- Options: (a) keep and record the definition question (preferred, container and wagon demurrage being established rail practice); (b) move the text.
- Needs decision: yes

### rail/08#F12 · Low · Passenger quantity 0 on a freight train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: PassengerQuantity is "the total number of passengers aboard a transport means"; a container train carries none by its nature, and stating 0 in a consignment note has no business reason (IND5/IND6). Same in rail/03#F9.
- Condition: PassengerQuantity is absent unless the story gives a reason.
- Options: remove it (preferred).
- Needs decision: no

### rail/08#F13 · Low · Container still "being stored" at the hub, and a stale estimate, in a document issued after departure
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:StorageLocation/cbc:Name` = `Ferrano Intermodal Hub, stack C`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DispositionCode` = `LOADED`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`
- Why: StorageLocation is "the location where this piece of transport equipment is being stored". At the issue time (13:10) the container is loaded (disposition LOADED, loading 05:40) on a train that departed at 06:52; it is no longer stored in stack C. Likewise the estimated departure 06:50 is superseded by the actual departure 06:52 recorded in the same stage.
- Condition: The equipment's storage location and the stage's estimates describe the situation at the issue time, or are absent.
- Options: remove the storage location and the estimated departure (preferred); or, if the waybill is meant to be issued at takeover, move its issue time before the loading (see F3 and F6).
- Needs decision: no

### rail/08#F14 · Low · The equipment references the waybill itself
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ShipmentDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- XPath: `/Waybill/cbc:ID` = `FRC-WB-26-0334`
- Why: ShipmentDocumentReference is "a reference to a shipping document associated with this piece of transport equipment". The referenced document is the waybill in which the reference stands; it adds no information (IND5/IND6).
- Condition: The equipment's shipment document reference, if present, points to another document.
- Options: remove it (preferred).
- Needs decision: no

### rail/08#F15 · Low · The second container lacks the wagon and events that the first has
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:StowagePositionID` = `31 46 4521 042-3 / A`
- Why: For container FRXU1044175 the waybill gives the wagon and slot (A), the train, loading and unloading places, pickup, handling, loading and delivery events. For FRXU1044180, carried under the same note on the same train, it gives none of these, so the note does not say on which wagon or slot the second box travels, nor where it is loaded or delivered. A consignment note covering two containers describes both.
- Condition: Both containers carry their wagon/stowage position and at least the loading and unloading locations, or the waybill states once (at consignment or stage level) what applies to both.
- Options: (a) preferred: give the second container its wagon (e.g. slot B of the same wagon) and the same loading/unloading locations; (b) move what both share (places, delivery) to the consignment or stage and keep only the per-box data on the equipment.
- Needs decision: no

## Checked and consistent
- Check digits: containers FRXU1044175 and FRXU1044180 (ISO 6346) and GLN 9520610900015 pass check_ids.py; the wagon number 31 46 4521 042-3 passes the UIC self-check digit (weights 2-1-2-…, sum of digits 47, check digit 3; own calculation). Whether the owner code FRXU and the UIC country code 46 are assigned in the real registers could not be checked here.
- Weights: 7884 kg per loaded box = 3984 kg goods (7968 / 2) + 3900 kg tare, a normal tare for a 40-foot high cube (own knowledge: about 3.7–3.9 t); same values and seals as rail/06. Length 12 192 mm and size type 45G1 agree.
- Energy and emissions: 2 × 610 kWh = 1220 kWh electricity; 410 kg CO2e / 1220 kWh = 0.336 kg per kWh, a plausible grid factor. Per container slot (box 7.9 t plus about 11 t of wagon share, own estimate) 610 kWh at 0.02 kWh per gross tonne-km (own knowledge for electric freight) corresponds to about 1600 km; the journey of about 28 h (06:52 to 10:40 next day) at 50–60 km/h fits that order of magnitude.
- Equipment events in order: positioned 2026-04-12 08:00, picked up 2026-04-13 15:00, handled at the hub 18:30, loaded 2026-04-14 05:40, despatched 06:50, departed 06:52 (rail/05 agrees), delivery planned 2026-04-15 11:00 (rail/03, rail/07), latest delivery 2026-04-16 (rail/02, rail/03).
- Train FRC 4417, journey CT 4471, mode 2, means type 2302, direction WB, loading sequence 7, crew 2: as in rail/03. Contracted carrier ID FRC-CON-2026-005/88 matches the contract FRC-CON-2026-005 and call-off 88 in rail/03; DocumentReference FRC-TEP-26-0328 resolves to rail/03.
- Loading location Ferrano (XUFER) and unloading location Marrowdale (XBMRW) agree with the stage's instructions and the delivery location; the fictional country codes XU/XB lie in ISO 3166's user-assigned range, so the LOCODEs cannot be mistaken for real ones.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossVolumeMeasure` = `76.3`: "gross volume of this piece of transport equipment" might mean the external volume (12.192 × 2.438 × 2.896 m ≈ 86.1 m³) rather than the internal capacity — not settled, but either reading leaves F7 standing (83.6 m³ of benches exceeds the usable internal space); not kept as a separate finding.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OperatingParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: the hub as operator of a carrier-owned container — refuted: a terminal can operate the carrier's box pool at its site; nothing in the flow contradicts it.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DamageRemarks` = `Small dent in the left side panel, noted at pick-up; no effect on the cargo.`: damage noted at pick-up in a document issued later — refuted: the remark states when it was noted.

## Outside this review
- Timeline: the waybill is issued at 13:10 on the departure day, after the loading (05:40) and departure (06:52); whether a consignment note can be made out this late, and how it fits the transit declaration's 17:29, is for the cross-document review (see F6 for the reference itself).
