# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/03-TransportExecutionPlan.xml`, Git blob `10a1218954b5cf3553a1e440bbc205476072297d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0cafa9c 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### rail/03#F1 · High · Planned pickup lies before the service may begin
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- Why: ServiceStartTimePeriod is "The period within which the service must begin". The plan collects the boxes at Castrano on 13 April at 15:00 (the carrier haulage the Note describes), a day before the service may begin. The request has the same contradiction (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`).
- Condition: The planned pickup lies within the service start period.
- Options: (a) preferred: start the period on 2026-04-13 (request and plan); (b) plan the pickup on 14 April.
- Needs decision: no

### rail/03#F2 · High · ToLocation is the hub, but the plan delivers to the siding in Marrowdale
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: ToLocation is "The destination location for the transport service referenced in the Transport Execution Plan". The plan's main carriage is a rail stage that ends in Marrowdale, where the containers are shunted to Lumeway's siding and delivered on 15 April; the contract describes slots "between the Ferrano hub and Marrowdale". The hub is where the haulage leg ends and the rail stage begins, not the destination of the service.
- Condition: ToLocation is where the planned service ends (Lumeway's siding, Marrowdale), or the plan covers only the haulage and carries no rail stage and delivery.
- Options: (a) preferred: ToLocation = Lumeway's rail siding, Marrowdale (GLN 9520610900015 as on the waybill); (b) split the plan.
- Needs decision: no

### rail/03#F3 · High · Main service "Full truck load" contradicts the rail stage
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- Why: FTL is "One truck for one consignment, from the place of loading to the place of delivery" (world TransportServiceCode list); the main carriage of the same plan is by rail (mode 2, a container train, TrainID FRC 4417), and the itinerary for this plan calls the service a container train (`09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`). The truck leg is the carrier haulage (CARRHAUL in the same list).
- Condition: MainTransportationService describes the rail main carriage and agrees with the itinerary; the haulage, if stated, is an AdditionalTransportationService.
- Options: (a) preferred: RAILCONT as main service, CARRHAUL as additional; (b) RAILWAGON if a whole wagon is meant.
- Needs decision: no

### rail/03#F4 · High · Payment terms of the plan contradict the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- Why: The plan agrees 30 days net counted from the consignment note, issued on 14 April (`08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`), so payment falls due on 14 May. The freight invoice instead sets 30 days from its own date with a 2 % discount (`10-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-17`; `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`).
- Condition: The terms agreed in the plan and the terms applied in the freight invoice agree (due date and any discount).
- Options: (a) preferred: let the invoice apply the plan's terms (due 2026-05-14, no discount) or let the plan state the invoice's terms; (b) explain a deviation in the invoice.
- Needs decision: no

### rail/03#F5 · Medium · One framework contract under two identifiers
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`
- Why: The document-level contract is a framework transport agreement (version 2, amended for ten more slots a month, call-off 88) whose contract document is FRC-CON-2026-005-A1, evidently amendment 1 of FRC-CON-2026-005. The consignment's contract is FRC-CON-2026-005, "Framework contract for container slots". These are the same framework contract, yet the contract itself is identified as VI-FRC-FW-2026. The waybill's ContractedCarrierAssignedID `FRC-CON-2026-005/88` also links call-off 88 to FRC-CON-2026-005.
- Condition: The same contract has one identifier in the plan (and the flow), or the plan states how the two identifiers relate.
- Options: (a) preferred: TransportContract/ID = FRC-CON-2026-005 at both levels, version 2 with the amendment as ContractDocumentReference; (b) if VI-FRC-FW-2026 is Valdara's own number, keep it only where Valdara is the issuer and say so.
- Needs decision: no

### rail/03#F6 · Medium · Late-payment surcharge used for late delivery
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PenaltySurchargePercent is "The penalty for payment after the settlement period, expressed as a percentage of the payment". The note makes it a penalty on the carrier for late delivery (per day late, capped at 25 %), which is a different obligation of a different party.
- Condition: PenaltySurchargePercent is absent, or it states a late-payment surcharge; the late-delivery penalty is expressed in text (or another fitting element).
- Options: (a) preferred: keep the late-delivery penalty only in the Note (PenaltyPaymentTerms "applying to a penalty specified in the transport execution plan" fits a penalty in general); (b) state a real late-payment surcharge if the contract has one.
- Needs decision: no

### rail/03#F7 · Medium · AtLocation names the carrier and no stationary service exists
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does not require transport movement". The plan has no such service (main service and the pre-arrival notice only), and the value is the name of the carrier, not of a place.
- Condition: AtLocation is absent, or it names the place of a stationary service the plan contains.
- Options: (a) preferred: drop it; (b) if terminal handling at the hub is part of the plan, add it as a service and give the hub as AtLocation.
- Needs decision: no

### rail/03#F8 · Medium · Province given in Region
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity), as the Bayvarran states are given in the same document. 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as a non-administrative region.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/03#F9 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` is a language, not a locale.
- Condition: LocaleCode absent or a locale (e.g. `en-XB`).
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/03#F10 · Medium · A gate in AdditionalStreetName
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is not a street, and the delivery is by rail to a siding.
- Condition: AdditionalStreetName holds a street name or is absent.
- Options: (a) preferred: drop it; (b) move access details to a delivery location.
- Needs decision: no

### rail/03#F11 · Low · Nomination deadline and nomination period disagree; contract time without date
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationDate` = `2026-04-08`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationTime` = `09:00:00`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:NominationPeriod/cbc:EndDate` = `2026-04-12`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:IssueTime` = `10:00:00`
- Why: NominationDate is "the deadline date by which the services ... have to be booked" (8 April 09:00), while NominationPeriod, "the period required to book the services ... before the services can begin", runs to 12 April. A booking deadline of 8 April and a booking period lasting until 12 April cannot both hold. The contract's IssueTime (10:00) has no IssueDate, so it identifies no point in time.
- Condition: The nomination deadline lies at the end of (or is consistent with) the nomination period; IssueTime appears only with IssueDate.
- Options: (a) preferred: one of the two (deadline 8 April 09:00 fits the request of 7 April and the plan of 8 April) and drop the other; give the contract's issue date with the time, or drop the time.
- Needs decision: no

### rail/03#F12 · Low · Post-event duration on a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- Why: PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given event and the issuance of a notification". A pre-arrival notice is issued before the arrival (the two hours of PreEventNotificationDurationMeasure, also in the remarks "notice two hours before arrival"); a notice one hour after the event is not described anywhere.
- Condition: Only the pre-event duration is given, or a second, post-event notification is described.
- Options: (a) preferred: drop the post-event duration; (b) add a separate arrival notification with that duration.
- Needs decision: no

### rail/03#F13 · Low · Filler and incomplete values in the terms and stage
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- Why: A freight train carries no passengers; stating zero adds nothing (IND5/IND6: nothing implied by absence, no fillers). The waiting-time charge of "40 per hour" gives no currency, so the amount cannot be applied.
- Condition: PassengerQuantity is absent; the waiting-time charge states its currency (e.g. XUF).
- Options: (a) preferred: drop PassengerQuantity; write "XUF 40 per hour" (or the right amount).
- Needs decision: no

### rail/03#F14 · Low · FromLocation named after the company; contacts do not fit the roles
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The location is named after the warehouse operator, while the waybill names the place "Castrano Logistics warehouse, Ferrano". The receiver of the plan (the transport user) is reached at its sales order desk and the consignee at its sales customer service, neither of which books or receives transport.
- Condition: The location is named as a place; the transport user's and the consignee's contacts are logistics/receiving functions (or absent).
- Options: (a) preferred: name the place as on the waybill; role-specific contacts.
- Needs decision: no

## Checked and consistent
- Reference: `VI-TR-26-0326` resolves to 02 (TransportExecutionPlanRequest, Valdara to Ferrano Rail Cargo); parties, consignment, weight, remarks and notes agree; the plan answers before the requested deadline (02: 2026-04-08; plan issued 2026-04-08 16:46).
- Times: planned departure 14 April 06:45 and arrival 15 April 10:30, estimated 06:50 and 10:40, planned delivery 15 April 11:00, all within the validity period (8 to 17 April) and before the requested delivery (16 April) and the contractual latest delivery date (16 April). The same planned and estimated times are reported in 05 and 08.
- The train identification (JourneyID CT 4471, TrainID FRC 4417, mode 2, type 2302 "Train, container") is the same in 04, 05, 08.
- BillToParty Valdara and the prepaid note "Freight prepaid by the consignor under DAP" agree with the order's DAP (01) and the freight invoice (10).
- Parties described as in the other rail examples.

## Considered and refuted
- `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`: suspected a contradiction because departure (06:45 instead of 07:00) and delivery (15 instead of 16 April) differ from the request — refuted because both are earlier than requested and within the requested windows, so the plan meets the request.
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-09`: suspected pointless with status Confirmed — refuted because a confirmed plan may still need the user's acceptance; a deadline for it is meaningful.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`: suspected an estimate that should not differ from the plan in the plan itself — refuted because a plan may carry the carrier's current estimate next to the timetable.
- `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`: suspected copied master data — refuted because the boxes are collected at Castrano's warehouse.
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotifyParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: suspected the wrong party for a pre-arrival notice — refuted because the arrival announced is that of the tractor with the boxes at the hub, which the hub needs to know.
