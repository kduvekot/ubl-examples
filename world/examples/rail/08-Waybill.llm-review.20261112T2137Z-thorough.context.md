# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

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

### rail/08#F1 · High · A road consignment note (CMR) for carriage by rail
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `FRC-CMR-26-0325`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`
- Why: WaybillTypeCode is "the type of waybill (Bill of Laden, Airwaybill, CMR, House waybill, Master waybill …)", and the world's list distinguishes CMR ("A consignment note under the Convention on the Contract for the International Carriage of Goods by Road") from CIM ("Rail consignment note … International Carriage of Goods by Rail"). The waybill's main carriage is by rail (mode 2, container train FRC 4417, shunting to the consignee's siding), across the Urvania–Bayvarra border. A CMR covers carriage by road; only the collection by tractor to the hub is road carriage, and that is domestic. The document type contradicts the carriage it documents (CIM is used for rail in another flow: one CIM over `*.xml`, `grep -rh --include='*.xml' WaybillTypeCode`).
- Condition: the waybill type, its name and the carrier's reference agree with the mode of the main carriage it documents.
- Options: (a) preferred: CIM, with a name and carrier reference to match; (b) a CMR only for the road leg, as a separate document, leaving the rail leg to a CIM.
- Needs decision: no

### rail/08#F2 · High · Shipment gross weight excludes the containers that its definition includes
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport equipment". The two loaded containers weigh 2 × 7884 = 15768 kg; 7968 kg is the goods' weight with packing (as in the consignments of rail/02 and rail/03). Tare implied: 3900 kg per 40-foot high cube, plausible.
- Condition: Shipment/GrossWeightMeasure = 15768 kg (goods + packaging + containers), or absent.
- Options: (a) preferred: 15768 kg; (b) drop it and keep the goods weight at consignment level.
- Needs decision: no

### rail/08#F3 · Medium · The rail wagon is given as contained in the container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:ID` = `31 46 4521 042-3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ContainedInTransportEquipment/cbc:TransportEquipmentTypeCode` = `RR`
- Why: ContainedInTransportEquipment is "a piece of transport equipment contained in this piece of transport equipment". The container is carried on the rail car; the rail car is not inside the container. The element states the relation the wrong way round. The wagon is already identified where it belongs: ApplicableTransportMeans/RailTransport/RailCarID and the StowagePositionID. The second container has no such relation, so the two containers are described differently.
- Condition: no equipment is stated to be contained in a container unless it is inside it.
- Options: (a) preferred: drop ContainedInTransportEquipment (the wagon is given by RailCarID and stowage position); (b) describe the wagon as a piece of equipment of its own in the consignment that carries the container, if a direct relation is wanted.
- Needs decision: no

### rail/08#F4 · Medium · The customs authority as issuer of the trader's transit declaration
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: IssuerParty is "the Party who issues this Customs Declaration". The declaration VI-TD-26-0331 is made and signed by Valdara (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`, TransitExporterParty "who makes the Transit Customs Declaration"); the customs administration receives and processes it (its CustomsParty).
- Condition: the issuer of the referenced declaration is the party that made it, as in rail/06.
- Options: (a) preferred: Valdara as IssuerParty; (b) drop IssuerParty.
- Needs decision: no

### rail/08#F5 · Medium · Distribution of the originals contradicts the note
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: DocumentDistribution is "a list of interested parties to whom this document is distributed", and its Party "the interested Party who receives this Document". The note says there are three originals, for consignor, consignee and carrier. The distribution sends "the consignee's original" to the hub (not the consignee), gives the consignor only an electronic copy (whose list text says "the original is held or sent elsewhere"), and lists nothing for the carrier.
- Condition: the distribution list and the note describe the same originals and recipients.
- Options: (a) preferred: the consignee's original with the goods to Lumeway Distribution, an original to Valdara, and the carrier's original kept by Ferrano Rail Cargo (or the note reduced to what is distributed); (b) change the note to match the list.
- Needs decision: no

### rail/08#F6 · Medium · Waypoints without a location
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedWaypointTransportEvent/cbc:OccurrenceTime` = `13:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- Why: A waypoint is "the location of an actual waypoint during a transportation service" / "a waypoint planned". Without a location the two times say nothing. The request named the waypoint (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`).
- Condition: each waypoint event has its location.
- Options: (a) preferred: add the border station as location to both.
- Needs decision: no

### rail/08#F7 · Medium · LocaleCode holds a bare language code
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639) names no locale. 362 occurrences over `*.xml`.
- Condition: a locale (e.g. `en-XB`) or absent.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/08#F8 · Medium · Province in Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/08#F9 · Low · Waybill description describes the road collection, not the contents
- XPath: `/Waybill/cbc:Description` = `Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.`
- Why: Waybill/Description is "text describing the contents of the Waybill". The text describes how the containers reach the hub, which is at most a note about pre-carriage; the contents are 192 benches in two containers by rail to Marrowdale. Together with F1 it makes the document read as a road document.
- Condition: the description, if present, describes what the waybill covers.
- Options: (a) preferred: describe the consignment and carriage (or drop it; the summary is in Consignment/SummaryDescription).
- Needs decision: no

### rail/08#F10 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- Why: IssueLocation is "the location where this waybill was issued". A company name is not a place (the checklist for Location); the waybill is issued by the carrier (SenderParty Ferrano Rail Cargo), and the goods were collected at Castrano's warehouse the day before.
- Condition: the issue location names a place (e.g. "Castrano Logistics warehouse, Ferrano" or the town).
- Options: (a) preferred: the place where the carrier issues the waybill.
- Needs decision: no

### rail/08#F11 · Low · Share listing of the waybill's receiver
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing`
- Why: The share listing of Valdara has no use in a waybill. (Its ServiceProviderParty Castrano Logistics is used: Castrano is the loading-proof party and pickup place.)
- Condition: no party data without a reason in the waybill.
- Options: (a) preferred: drop the listing here.
- Needs decision: no

### rail/08#F12 · Low · Performing carrier identical to the contracted carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:PerformingCarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:PerformingCarrierAssignedID` = `FRC-J-26-3318`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ContractedCarrierAssignedID` = `FRC-CON-2026-005/88`
- Why: The performing carrier is a role that matters when another carrier performs the carriage than the one contracted. Here both are Ferrano Rail Cargo, which gives the consignment two identifiers of its own in two roles. This reads as a filler for the performing-carrier elements.
- Condition: performing-carrier data is present only when a different carrier performs (all or part of) the carriage.
- Options: (a) preferred: drop PerformingCarrierParty and PerformingCarrierAssignedID; (b) a different performing carrier (e.g. a Bayvarran rail operator beyond the border), which changes the story.
- Needs decision: no

### rail/08#F13 · Low · Zero passengers on a freight train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: A container train carries no passengers; zero passengers has no business reason in a waybill for freight (filler, rule IND5/IND6). The same value is in the plan rail/03.
- Condition: PassengerQuantity is absent where the means carries no passengers by its nature.
- Options: (a) preferred: drop it.
- Needs decision: no

### rail/08#F14 · Low · Estimated departure after the actual departure is known
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- Why: The waybill is issued at 13:10, after the actual departure at 06:52; the estimate of 06:50 is stale and has no use next to the actual time.
- Condition: no estimate for an event whose actual time the document reports.
- Options: (a) preferred: drop the estimated departure.
- Needs decision: no

### rail/08#F15 · Low · Storage location for a container that is on the train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:StorageLocation/cbc:Name` = `Ferrano Intermodal Hub, stack C`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DispositionCode` = `LOADED`
- Why: StorageLocation is "the location where this piece of transport equipment is being stored". At issue (14 April 13:10) the container has been loaded on the wagon (05:40) and has left with the train (06:52); it is not being stored in stack C. The stack was where it waited overnight after the handling event on 13 April 18:30.
- Condition: StorageLocation is absent, or the document states it as a past storage (e.g. through the handling event's location).
- Options: (a) preferred: move "stack C" to the HandlingTransportEvent's location; (b) drop it.
- Needs decision: no

### rail/08#F16 · Low · Container not under the Container Convention while travelling under customs seal
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:LegalStatusIndicator` = `false`
- Why: LegalStatusIndicator is "an indication of the legal status of this piece of transport equipment with respect to the Container Convention Code". The containers cross a border under external transit with seals that "remain intact" (rail/06). Under the Customs Convention on Containers (own knowledge), containers approved for transport under customs seal carry that status; "false" says this one does not, which is at odds with the transit under seal. The indicator's meaning is not precise in UBL, so it may also simply be a filler.
- Condition: the indicator is absent, or true for a container used for transit under customs seal (or the story explains why it is not approved).
- Options: (a) preferred: drop it; (b) true.
- Needs decision: yes

### rail/08#F17 · Low · The waybill references itself as shipping document of the container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ShipmentDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- Why: ShipmentDocumentReference is "a reference to a shipping document associated with this piece of transport equipment". The only document given is this waybill (`/Waybill/cbc:ID` = `FRC-WB-26-0334`); the reference adds nothing, and the second container has none.
- Condition: the reference points to another document, or is absent.
- Options: (a) preferred: drop it; (b) reference a document of its own for the container (e.g. an equipment interchange receipt), if the world has one.
- Needs decision: no

### rail/08#F18 · Low · Emission calculation location is an office, not a geographical context
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionCalculationLocation/cbc:Name` = `Ferrano Rail Cargo, energy office`
- Why: EmissionCalculationLocation is "the geographical context in which this environmental emission was calculated or for which the emission factor applies, such as the country of a national database or regulatory regime". The office that did the calculation is not such a context; for electric traction the relevant context is the grid (Urvania, or the Trade Accord grid) whose emission factor applies.
- Condition: the location is the geographic context of the factor (a country or grid region), or the element is absent.
- Options: (a) preferred: the country/grid whose electricity factor was used; (b) drop it.
- Needs decision: no

## Checked and consistent
- Seals, container IDs (ISO 6346 check digits pass), size type 45G1 and length 12192 mm agree with each other and with rail/06.
- Gross volume 76.3 m³ for a 40-foot high cube (internal volume about 76 m³, own knowledge): plausible.
- Energy and emission: 2 × 610 kWh = 1220 kWh for 410 kg CO2e gives 0.34 kg/kWh, a plausible grid factor for electric traction (own knowledge).
- Pickup 13 April 15:00 at the Castrano warehouse, handling 18:30, loading on the wagon 05:40, despatch 06:50 and departure 06:52: in order, and the pickup agrees with the plan rail/03.
- References: `/Waybill/cac:DocumentReference/cbc:ID` = `FRC-TEP-26-0328` is rail/03; the customs declaration VI-TD-26-0331 is rail/06 (issuer aside, F4).
- Freight per container 54600 XUF agrees with the price per container slot in the invoice rail/10.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cbc:ContractedCarrierAssignedID` = `FRC-CON-2026-005/88`: suspected a contract number used as a consignment ID — refuted because the call-off number under the framework contract (call-off 88, rail/03) is how the contracted carrier identifies this consignment.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:PowerIndicator` = `false`: suspected filler — refuted because it states a property of the equipment explicitly (a dry container has no power supply), which is not implied by absence.
- `/Waybill/cbc:AdValoremIndicator` = `false`: suspected filler — refuted because the indicator states that no ad valorem freight applies, which a waybill legitimately says.

## Outside this review
- Timeline: the waybill (issued 14 April 13:10) cites the transit declaration VI-TD-26-0331, which is issued only at 17:29 that day (rail/06), and a consignment note normally exists before the goods are taken over (13 April 15:00).
