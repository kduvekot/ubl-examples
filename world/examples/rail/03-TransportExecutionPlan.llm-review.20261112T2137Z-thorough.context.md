# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

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

### rail/03#F1 · High · Planned pickup lies before the period in which the service must begin
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "the period within which the service must begin". The provider plans to collect the containers at Castrano Logistics on 13 April 15:00 ("Collection as requested"), so the service it confirms begins a day before the period opens.
- Condition: the planned pickup lies within the service start period.
- Options: (a) preferred: start the period on 2026-04-13; (b) plan the road collection as a separate service.
- Needs decision: no

### rail/03#F2 · High · Main service "Full truck load" contradicts the itinerary governed by this plan
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:Name` = `Full truck load`
- Why: FTL is "One truck for one consignment, from the place of loading to the place of delivery". This plan confirms carriage of two 40-foot containers on the container train (TransportMeansTypeCode 2302 "Train, container", TransportModeCode 2), and the goods item itinerary whose segment is governed by this plan says RAILCONT: `09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cbc:TransportExecutionPlanReferenceID` = `FRC-TEP-26-0328` with `09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`.
- Condition: the main transportation service of the plan is the container train service, consistent with the itinerary.
- Options: (a) preferred: RAILCONT as main service, the road collection as an additional service; (b) none other that keeps the plan and the itinerary consistent.
- Needs decision: no

### rail/03#F3 · Medium · From and To locations describe the road collection only
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`
- Why: ToLocation is "the destination location for the transport service referenced in the Transport Execution Plan". The plan delivers to the Lumeway siding in Marrowdale on 15 April 11:00 after the train's arrival at 10:30; the contract it is called off under covers "Container slots between the Ferrano hub and Marrowdale". The hub is where the containers change from road to rail.
- Condition: ToLocation is where the planned service ends.
- Options: (a) preferred: ToLocation = the Lumeway siding, Marrowdale; (b) separate plans per leg.
- Needs decision: no

### rail/03#F4 · Medium · AtLocation without a stationary service, holding a company name
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "the location of a transport service (e.g., terminal handling service) that does not require transport movement". The plan contains no such service (its additional service is a pre-arrival notice), and the value is the name of the provider, not a place.
- Condition: AtLocation is present only for a service without movement that the plan contains, and names that place.
- Options: (a) preferred: drop it; (b) if terminal handling at the hub is part of the service, add that service and give the hub as AtLocation.
- Needs decision: no

### rail/03#F5 · Medium · Late-payment surcharge percent used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PenaltySurchargePercent is "the penalty for payment after the settlement period, expressed as a percentage of the payment". The note describes a penalty on the carrier for late delivery (a reduction of the freight per day of delay), not a surcharge on the payer for paying late. PenaltyPaymentTerms ("terms of payment applying to a penalty specified in the transport execution plan") fits the late-delivery penalty; the percent element does not.
- Condition: PenaltySurchargePercent is absent, or describes a late-payment surcharge.
- Options: (a) preferred: keep the late-delivery penalty in the Note only (no UBL element defines a delay penalty percent); (b) a late-payment surcharge, if the story has one.
- Needs decision: no

### rail/03#F6 · Medium · Pre-arrival notification with a post-event duration
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: PostEventNotificationDurationMeasure is "the length of time between the occurrence of a given event and the issuance of a notification". A pre-arrival notice is issued before the event (two hours, as the remarks say: "notice two hours before arrival"); a notification one hour after the arrival is a different requirement that nothing in the plan describes.
- Condition: the requirement carries only the timing that its type needs (pre-event for a pre-arrival notice), or a second requirement of its own type states the post-event notice.
- Options: (a) preferred: drop the post-event duration; (b) a separate NotificationRequirement (e.g. arrival confirmation) with it.
- Needs decision: no

### rail/03#F7 · Medium · LocaleCode holds a bare language code
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639) names no locale. 362 occurrences over `*.xml`.
- Condition: LocaleCode is a locale (e.g. `en-XB`) or absent.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/03#F8 · Medium · Province in Region
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a "geographic or economic region or group of countries" (Region).
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/03#F9 · Low · Two identifiers for what reads as the same framework contract
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`
- Why: The document-level contract is a "Framework transport agreement" whose contract document is FRC-CON-2026-005-A1 (by its form, amendment 1 of FRC-CON-2026-005), described as "Container slots between the Ferrano hub and Marrowdale". The consignment's contract FRC-CON-2026-005 is a "Framework contract for container slots". Either they are the same contract under two identifiers (then one identifier should be used, or the relation stated), or two contracts, and then the plan does not say how they relate. The waybill uses FRC-CON-2026-005 only (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`).
- Condition: the framework contract is identified the same way wherever it is meant, or the two contracts are distinguishable by their descriptions.
- Options: (a) preferred: one contract identifier throughout, the amendment as its contract document; (b) keep two contracts and describe the difference.
- Needs decision: yes

### rail/03#F10 · Low · Nomination deadline before the end of the nomination period
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationDate` = `2026-04-08`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationTime` = `09:00:00`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:NominationPeriod/cbc:EndDate` = `2026-04-12`
- Why: NominationDate is "the deadline date by which the services … have to be booked"; NominationPeriod is "the period required to book the services … before the services can begin". A booking period that runs to 12 April and a booking deadline of 8 April 09:00 say different things about when booking closes.
- Condition: the nomination deadline and the nomination period agree (the deadline is the period's end, or the two are explained).
- Options: (a) preferred: keep one of the two; (b) align the dates.
- Needs decision: no

### rail/03#F11 · Low · Zero passengers on a freight train
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: A container train carries no passengers; stating zero has no business reason in a transport plan for freight (filler, rule IND5/IND6). The same value occurs in the waybill.
- Condition: PassengerQuantity is absent where the means carries no passengers by its nature.
- Options: (a) preferred: drop it.
- Needs decision: no

### rail/03#F12 · Low · Share listing of the transport user in a transport plan
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing`
- Why: The share listing of Valdara plays no part in the plan.
- Condition: no party data without a reason in the plan.
- Options: (a) preferred: drop it here.
- Needs decision: no

## Checked and consistent
- The plan answers the request: `/TransportExecutionPlan/cac:TransportExecutionPlanRequestDocumentReference/cbc:ID` = `VI-TR-26-0326` is rail/02; status Confirmed with reason "As requested" agrees with pickup, departure and delivery dates within the requested window (request: delivery 16 April, plan: 15 April).
- Bill-to party Valdara and the note "Freight prepaid by the consignor under DAP" agree with the Incoterm of the order (rail/01).
- The pre-arrival notification to Ferrano Intermodal Hub agrees with the additional service NOTIFY and the provider remarks.

## Considered and refuted
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions` = `Free time five days at the siding, then demurrage per container day.`: suspected misuse because UBL's definition speaks of a vessel — refuted because demurrage of containers and wagons is the same concept in rail and intermodal practice, and the element is in a shipment stage of any mode.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`: suspected that an estimate six days ahead is out of place in a plan — refuted because the plan may carry the provider's forecast next to the timetable time; the five minutes' difference is plausible.
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected copied text — refuted because the plan repeats the user's remarks by definition ("remarks from the transport user").
