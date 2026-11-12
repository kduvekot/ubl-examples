# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/03-TransportExecutionPlan.xml`, Git blob `b9cd241a833ef55a0d6d59ac19ae0579457b6de6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/03#F1 · High · Container train planned for ore carried loose in wagons
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: `RAILCONT` means "Containers on a scheduled container train" (world list
  TransportServiceCode). The plan references a wagon list
  (`/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`), the goods
  are "loose in rail wagons" (01-Order.xml, 04-DespatchAdvice.xml), the despatch line counts
  30 wagons (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`)
  and the carrier's own invoice for this plan bills "Rail freight, ore in bulk wagons"
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`).
  The plan therefore contradicts the invoice that refers to it.
- Condition: the main transportation service describes carriage of bulk ore in wagons and agrees with
  02-TransportExecutionPlanRequest.xml and 06-Invoice.xml.
- Options: (a, preferred) `RAILWAGON` ("A whole wagon for one consignment") with a matching name;
  (b) a new world code for a whole (block) train.
- Needs decision: no

### ore/03#F2 · High · Pre-arrival notification period lies before the transport
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:EndDate` = `2026-03-08`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: `NotificationPeriod` is "a period during which a notification will be issued". The
  notification is a pre-arrival notice given two hours before arrival
  (`/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`;
  `/TransportExecutionPlan/cbc:TransportServiceProviderRemarks` = `Collection as requested; notice two hours before arrival.`).
  The train cannot arrive before the service starts on 2026-03-10 (the waybill is issued
  2026-03-10 11:35), so a notice issued two hours before arrival falls between 2026-03-10 and
  2026-03-13, never in 2026-03-04 to 2026-03-08.
- Condition: the notification period covers the possible arrival times (within 2026-03-10 to
  2026-03-13), or is left out.
- Options: (a, preferred) 2026-03-10 to 2026-03-13, the service window; (b) remove the period, since
  the two-hour lead time already fixes when the notice is issued.
- Needs decision: no

### ore/03#F3 · Medium · Plan "as requested" drops the requested weighing and sheeting
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonDescription` = `Capacity available on the requested day.`
- XPath: `/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `WEIGH`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`
- Why: the plan confirms the request "as requested", but the weighing service the user requested
  (with tariff class `B`) is not in the plan, and the transport user's special term "Wagons sheeted
  against dust" is replaced by a different user term. `TransportUserSpecialTerms` is "text
  describing special terms specified by the transport user": the user did not specify the new text
  in the request. The reason text speaks of "the requested day", while the request asked for a
  window (2026-03-10 to 2026-03-13). The weight on the waybill (1788.4 t) suggests the train was
  weighed, but the plan does not say so.
- Condition: either the plan contains the requested weighing service and the user's sheeting term
  (so that "as requested" holds), or the status reason states that the plan differs from the
  request and how; the reason text refers to the requested window.
- Options: (a, preferred) keep the requested `WEIGH` service next to `NOTIFY` and carry the user's
  term "Wagons sheeted against dust." (adding the delivery-slot term if the user agreed to it);
  (b) change the status reason to a modification and describe the change.
- Needs decision: no

### ore/03#F4 · Medium · Pre-arrival notice with a post-event duration
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: `PostEventNotificationDurationMeasure` is "the length of time between the occurrence of a
  given event and the issuance of a notification", `PreEventNotificationDurationMeasure` "the
  length of time to elapse between the issuance of a notification and the occurrence of the event
  it relates to". One notification of type pre-arrival cannot be issued both two hours before and
  one hour after the arrival. No text in the plan mentions a notice after arrival.
- Condition: the notification requirement for the pre-arrival notice carries only the pre-event
  duration; a notice after arrival, if wanted, is a second notification requirement of its own type.
- Options: (a, preferred) remove the post-event duration; (b) add a second requirement (e.g. arrival
  confirmation) carrying the one-hour post-event duration, if the story needs it.
- Needs decision: no

### ore/03#F5 · Medium · Province given in Region in the transport locations
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries in which
  this address is located"; a province belongs in `CountrySubentity`. Same use at 219 places in
  104 examples (lxml over `*/*.xml`, `cbc:Region` values containing "Province").
- Condition: the province is in `CountrySubentity`.
- Options: (a, preferred) move it to `CountrySubentity` everywhere; (b) record a decision if
  intended.
- Needs decision: no

### ore/03#F6 · Low · At-location names the carrier, and no stationary service needs it
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: `AtLocation` is "the location of a transport service (e.g., terminal handling service) that
  does not require transport movement". The plan's only additional service is the pre-arrival
  notice, which has no place; the requested weighing at the mine siding (the request's
  `AtLocation` "Serravona mine siding") is not in the plan (F3). The value is a company name, not a
  place.
- Condition: `AtLocation` is present only for a stationary service in the plan and names its place.
- Options: (a, preferred) with the weighing service restored (F3), "Serravona mine siding" as in the
  request; (b) remove `AtLocation`.
- Needs decision: no

### ore/03#F7 · Low · Location names are party names
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Valdara Industries`
- Why: the places are the mine siding and the factory siding (06-Invoice.xml: "Ore from the mine
  siding to the factory siding"). `NotificationLocation` is "a location at which a notification
  will be issued": the carrier issues the notice from the train or its control office, not at the
  consignee. 46 places in 25 examples carry a party name as a location name (lxml over `*/*.xml`).
- Condition: the location names name places; the notification location is the place where the notice
  is issued, or is left out.
- Options: (a, preferred) siding names (with `XUSRV` for the mine); remove the notification location;
  (b) keep company names with a `SubsidiaryLocation` for the siding.
- Needs decision: no

### ore/03#F8 · Low · The plan does not say what is carried, and references only IDs
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
- XPath: `/TransportExecutionPlan/cac:TransportServiceDescriptionDocumentReference/cbc:ID` = `FRC-TSD-26`
- XPath: `/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`
- Why: the agreed plan describes the consignment only by its weight; the goods are named only in the
  note ("The ore train"), and the 30 wagons only in an external wagon list. None of the three
  references resolves to an example (`flow_index.py ore`), and the additional reference carries no
  type code or text saying it is a wagon list.
- Condition: the consignment says what is carried (goods item or description, HS `260111`) and, if the
  plan agrees the wagons, their number; the additional reference states its type.
- Options: (a, preferred) a goods item with description and HS code, and `DocumentTypeCode` or
  `DocumentType` on the wagon-list reference; (b) a consignment-level description only.
- Needs decision: yes (whether the standing plan FRC-TEP-26-0001 and service description should
  exist as examples)

## Checked and consistent
- Request reference `VI-TR-26-0305` resolves to 02-TransportExecutionPlanRequest.xml; parties,
  consignment ID, gross weight, service window (2026-03-10 to 2026-03-13), locations and transport
  contract `VI-FRC-FW-2026` agree with it.
- Dates: issued 2026-03-04 12:50, within the provider's response deadline (2026-03-04); validity
  2026-03-04 to 2026-03-13 covers the service window; user response by 2026-03-05.
- The bonus "first day of the window" refers to 2026-03-10, the service start.
- Physics, emissions: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:EnvironmentalEmission/cbc:ValueMeasure` = `1.9`
  t CO2e for 1800 t is 1.06 kg CO2e/t. With rail-freight factors of about 15–25 g CO2e/tkm for
  diesel bulk trains (own knowledge, GLEC/EN 16258 order of magnitude) this corresponds to
  42–70 km, plausible for two places in the same province (postal zones 4110 and 4120). The distance
  itself could not be checked: no example gives the factory's coordinates or the route length.
- Physics, wagons: 1800 t in about 30 wagons of 60 t (04-DespatchAdvice.xml); see 01-Order.xml review
  for volume and axle load (60 t lump ore ≈ 21–26 m³; 82–85 t gross per 4-axle wagon).
- `DeliveryTerms` `FCA` agrees with 01-Order.xml.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-03-05` on a
  plan already `Confirmed`: suspected contradiction — refuted because a plan confirmed by the provider
  can still await the user's acceptance; the deadline is after the issue date.
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected the
  provider writing the user's remarks — refuted because it repeats the user's remark from
  02-TransportExecutionPlanRequest.xml unchanged, as the element allows.
- `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000` against the actual
  1788.4 t: refuted, the plan states the planned weight before loading.

## Outside this review
- Whether 30 wagons are available on 2026-03-10 and the route from Serravona to Ferrano exists on the
  map (capacity, route) is for the consistency review.
