# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/03-TransportExecutionPlan.xml`, Git blob `10a1218954b5cf3553a1e440bbc205476072297d` (committed)
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

### rail/03#F1 · High · The plan's service and route are a truck run to the hub, its consignment a container train to Marrowdale
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:Description` = `Container slots between the Ferrano hub and Marrowdale.`
- Why: MainTransportationService is the "description of the main transportation service referenced in the Transport Execution Plan" and ToLocation "the destination location for the transport service". The plan confirms a full truck load from the warehouse to the Ferrano hub, while its own consignment is carried by rail (mode 2, container train FRC 4417) from the hub to the Lumeway siding in Marrowdale, under a contract for container slots between the hub and Marrowdale, with planned delivery on 2026-04-15. The itinerary that refers to this plan describes the segment it governs as a container train (`09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`), and the freight invoice bills container slots on the train. The truck leg, which the note describes as carrier haulage, has no pre-carriage stage. The same contradiction is in the request (rail/02).
- Condition: MainTransportationService, FromLocation and ToLocation describe the transport of the consignment's main carriage stage; the road leg from the warehouse to the hub, if part of the plan, is a pre-carriage stage with its own mode and events.
- Options: (a) preferred: main service RAILCONT, ToLocation the Lumeway siding in Marrowdale, a `cac:PreCarriageShipmentStage` (mode 3) carrying the planned pickup and the truck; (b) restrict the plan to the truck leg and move the rail transport to a plan of its own (changes the flow, and the waybill, itinerary and invoice refer to this plan for the rail part).
- Needs decision: yes

### rail/03#F2 · High · Planned pickup before the period in which the service must begin
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "the period within which the service must begin"; it starts on 2026-04-14, but the plan has the pickup, and with it the service, on 2026-04-13 at 15:00. The waybill confirms the actual pickup at that time (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cbc:ActualPickupDate` = `2026-04-13`).
- Condition: Every planned event of the service lies within or after ServiceStartTimePeriod.
- Options: (a) preferred: start the period on 2026-04-13; (b) if the period is meant for the rail main carriage only, that follows from fixing F1 (the pickup then belongs to a pre-carriage stage whose start is stated separately).
- Needs decision: no

### rail/03#F3 · Medium · AtLocation names the carrier, and the plan has no service without movement
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "the location of a transport service (e.g., terminal handling service) that does not require transport movement". Its value is the name of the transport service provider, not a place, and the plan describes no stationary service (no terminal handling or storage service among the main and additional services; the additional service is a pre-arrival notice).
- Condition: Either AtLocation is absent, or it names a place where a stationary service of this plan is performed, and that service is described in the plan.
- Options: (a) preferred: remove AtLocation; (b) if terminal handling at the hub is part of the plan, add it as an AdditionalTransportationService and set AtLocation to the Ferrano Intermodal Hub (with UN/LOCODE XUFER).
- Needs decision: no

### rail/03#F4 · Medium · Urvanian province in Region in the from and to locations
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this address is located"; a province belongs in CountrySubentity, as Bayvarran states are given in this flow. The value occurs 219 times in 104 examples (`grep -rh --include='*.xml' '<cbc:Region>Province of'`), so it looks like a convention for Urvania that the owner should confirm or change.
- Condition: An Urvanian province is in `cbc:CountrySubentity`, or the world states why it is a region.
- Options: (a) preferred: CountrySubentity; (b) keep and document the convention.
- Needs decision: yes

### rail/03#F5 · Low · The same framework contract has two identifiers in the plan
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`
- Why: The document-level contract is a framework transport agreement for container slots, version 2, call-off 88, whose contract document is FRC-CON-2026-005-A1 (amendment 1 of FRC-CON-2026-005). The consignment's contract is the framework contract for container slots FRC-CON-2026-005, and the waybill's contracted-carrier consignment ID combines that number with the call-off (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ContractedCarrierAssignedID` = `FRC-CON-2026-005/88`). The same contract therefore appears under VI-FRC-FW-2026 and FRC-CON-2026-005; a reader cannot tell whether these are one contract or two.
- Condition: One contract has one identifier throughout the flow, or the two identifiers are evidently different contracts (e.g. the buyer's own reference given as such).
- Options: (a) preferred: use FRC-CON-2026-005 as the contract ID in both places (the carrier's numbering, which the waybill uses); (b) if VI-FRC-FW-2026 is Valdara's own number, keep it in the request only.
- Needs decision: no

### rail/03#F6 · Low · Nomination deadline and nomination period disagree, and the contract has an issue time without a date
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationDate` = `2026-04-08`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationTime` = `09:00:00`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:NominationPeriod/cbc:EndDate` = `2026-04-12`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:IssueTime` = `10:00:00`
- Why: NominationDate/Time is "the deadline date by which the services referred to in the transport execution plan have to be booked"; NominationPeriod is "the period required to book the services specified in the contract before the services can begin". The deadline 2026-04-08 09:00 lies four days before the end of the booking period 2026-04-12, so they state two different last booking moments. The contract's IssueTime 10:00 has no IssueDate, so it identifies no point in time (the consignment's copy of the contract has the date 2026-01-05 and no time).
- Condition: The nomination deadline and the nomination period agree (the deadline is the end of the period, or one of them is absent), and the contract's issue time comes with its date or is absent.
- Options: (a) preferred: keep the deadline 2026-04-08 09:00 (the request came in before it) and end the nomination period on 2026-04-08, and remove the contract's IssueTime or add IssueDate 2026-01-05; (b) keep the period and remove the deadline.
- Needs decision: no

### rail/03#F7 · Low · Planned and estimated events of the main carriage without locations
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceTime` = `10:30:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedDeliveryTransportEvent/cbc:OccurrenceTime` = `11:00:00`
- Why: None of the plan's events has a location. With the plan's From/To locations pointing to the warehouse and the hub (F1), the reader cannot tell that the departure at 06:45 is from the hub and the arrival at 10:30 is in Marrowdale. The waybill does give the departure location (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`).
- Condition: Each planned departure, arrival, pickup and delivery names its place, or the stage's loading and unloading places make it unambiguous.
- Options: add `cac:Location` (name and UN/LOCODE XUFER / XBMRW, GLN of the siding) to the events, or LoadingPortLocation/UnloadingPortLocation to the stage (preferred: the events, as rail/08 does for the actual departure).
- Needs decision: no

### rail/03#F8 · Low · Pre-arrival notification with a post-event duration
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: PostEventNotificationDurationMeasure is "the length of time between the occurrence of a given event and the issuance of a notification". A pre-arrival notice is issued before the event (two hours, as the remarks say: "notice two hours before arrival"); a notice one hour after the arrival is a different notification that the plan does not describe. Nothing else in the plan explains the one hour.
- Condition: The notification requirement carries only the durations its type implies, or a second requirement describes the post-event notice.
- Options: (a) preferred: remove PostEventNotificationDurationMeasure; (b) add a separate NotificationRequirement for an arrival confirmation with the one-hour delay.
- Needs decision: no

### rail/03#F9 · Low · Passenger quantity 0 on a freight train
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: PassengerQuantity is "the total number of passengers aboard a transport means". A container train carries no passengers by its nature; stating 0 has no business reason in a transport plan (no fillers, IND5/IND6). The same is in `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`.
- Condition: PassengerQuantity is absent unless a reason to state it exists in the story.
- Options: remove it (preferred).
- Needs decision: no

### rail/03#F10 · Low · Demurrage instructions for containers at a siding, under a definition about vessels
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions` = `Free time five days at the siding, then demurrage per container day.`
- Why: UBL defines DemurrageInstructions as "text of instructions relating to demurrage (the case in which a vessel is prevented from loading or discharging cargo within the stipulated laytime)". The value concerns container free time at a rail siding, which trade calls demurrage too but which is not the vessel case of the definition. Whether the parenthesis restricts the element to vessels, or only gives an example, decides whether this is a misuse.
- Condition: Either the owner confirms the parenthesis is only an example (and records it as a UBL definition finding), or the container free time is stated elsewhere (e.g. in the transport execution terms or the equipment's information).
- Options: (a) keep and record as a definition question for the UBL TC (preferred, since container and wagon demurrage are established rail practice); (b) move the text to TransportExecutionTerms/TransportServiceProviderSpecialTerms.
- Needs decision: yes

## Checked and consistent
- References: TransportExecutionPlanRequestDocumentReference VI-TR-26-0326 resolves to rail/02, a request from the same transport user to the same provider; the plan's consignment ID, summary, weight (7968 kg) and parties agree with it.
- Times against the issue time (2026-04-08 16:46): all planned and estimated events lie after it; the provider's response deadline (2026-04-08) is met; the user's response deadline (2026-04-09) and the validity (2026-04-08 to 2026-04-17) cover the service up to the service end date 2026-04-17.
- Plan against the request: planned departure 06:45 (requested 07:00), planned arrival 2026-04-15 10:30 (requested 2026-04-15), planned delivery 2026-04-15 11:00 (requested 2026-04-16, contractual latest 2026-04-16): within what was asked, so "as requested" holds.
- Planned and estimated times agree with the progress status and the waybill: 06:45/06:50 departure, 10:30/10:40 arrival (rail/05, rail/08); train FRC 4417, journey CT 4471, loading sequence 7 and direction WB are the same in rail/08. Whether westbound is the direction from Ferrano to Marrowdale could not be checked from the examples.
- Transport means type 2302 (UNECE Rec. 28: container train) fits mode 2 and the container consignment.

## Considered and refuted
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `CT 4471` against `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`: transposed digits suggested a typing error — refuted: JourneyID is "an identifier for the regular service schedule", TrainID "an identifier for the train"; they are different identifiers and are used consistently in rail/04, rail/05 and rail/08.
- `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`: the plan departs 15 minutes earlier and delivers a day earlier than requested — refuted: both are within what the request asks (departure on 2026-04-14, delivery by 2026-04-16).
- `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`: does not resolve to an example — refuted as a broken reference: a contract amendment the flow does not model, named unambiguously.
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotifyParty`: the hub notified before "arrival" although the consignee unloads at Marrowdale — refuted as a separate problem: with the plan's destination being the hub (F1) the notice to the hub is consistent; after F1 is fixed, the fixing session should check whom the pre-arrival notice goes to.
