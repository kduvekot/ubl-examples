# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### ore/03#F1 · High · Container-train service planned for ore loose in wagons
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: `RAILCONT` means "Containers on a scheduled container train" in the world's
  TransportServiceCode list; the goods travel "loose in rail wagons"
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`),
  as "30 wagons of about 60 tonnes" (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note`),
  and the same carrier invoices "Rail freight, ore in bulk wagons"
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]`). The list has `RAILWAGON`
  "Rail wagon load". The plan contradicts the goods and the carrier's own invoice.
- Condition: the planned main service is a wagon-load (bulk) rail service, the same as in the
  corrected request `02-TransportExecutionPlanRequest.xml`.
- Options: (a, preferred) `RAILWAGON`; (b) a new code for a whole (block) train.
- Needs decision: no

### ore/03#F2 · High · Pre-arrival notifications scheduled before the train leaves
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:EndDate` = `2026-03-08`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: NotificationPeriod is "A period during which a notification will be issued". The
  notification is a pre-arrival notice two hours before arrival (`PREARRIVAL`, 2 HUR, and
  `TransportServiceProviderRemarks` "notice two hours before arrival"). The service begins on
  10 March and ends by 13 March, and the train is despatched on 10 March
  (`04-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-03-10`). A notice two hours before
  arrival cannot be issued between 4 and 8 March. The period contradicts the event it announces.
- Condition: the notification period covers the time two hours before the planned arrival (within
  the service period 10–13 March), or is left out.
- Options: (a, preferred) period 10–13 March (the service window); (b) leave out the period, since
  the pre-event duration already fixes when the notice comes.
- Needs decision: no

### ore/03#F3 · High · Plan confirmed "as requested" but differs from the request
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`
- XPath: `/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `WEIGH`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`
- Why: the plan is `Confirmed` with the reason "As requested" ("Capacity available on the requested
  day"), yet it drops the weighing service the request asked for, replaces the transport user's
  special terms (sheeting against dust) with other user terms, and changes the place of the
  stationary service from the mine siding to "Ferrano Rail Cargo". TransportUserSpecialTerms are
  "special terms specified by the transport user"; the user did not specify the terms the plan
  attributes to it. Either the plan is not as requested, or it misstates the request.
- Condition: the plan's services, user terms and service place agree with the request it confirms
  as requested, or the status reason and remarks say what was changed.
- Options: (a, preferred) carry the request's weighing service (with the mine siding as AtLocation)
  and the user's sheeting term into the plan, adding the provider's notification service and the
  slot/unloading terms as provider terms; (b) keep the changes and give a status reason that
  says the plan deviates, with the changes in the provider's remarks.
- Needs decision: no

### ore/03#F4 · High · Freight payment terms contradict the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `06-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-11`
- Why: the plan agrees payment 30 days net from the consignment note; the consignment note is dated
  10 March (`05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`), so payment is due on 9 April.
  The carrier's invoice for this transport counts 30 days from its own date (12 March → 11 April)
  and offers a 2 % settlement discount the plan does not have. The two documents describe the same
  freight payment differently.
- Condition: the plan's payment terms and the freight invoice's terms, due date and discount agree.
- Options: (a, preferred) align the invoice with the plan (due 9 April, no discount), since the plan
  is the agreed term; (b) state in the plan the terms the invoice applies.
- Needs decision: no

### ore/03#F5 · Medium · Late-payment surcharge element used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PaymentTerms/PenaltySurchargePercent is "The penalty for payment after the settlement
  period, expressed as a percentage of the payment". Here the penalty is the carrier's for
  delivering late ("5 % of the freight per day late"), not the payer's for paying late. The
  PenaltyPaymentTerms aggregate fits (terms of a penalty in the plan), but the percentage element
  carries another meaning. The same note with this element occurs in 3 `*.xml` files
  (`grep -rh --include='*.xml' -B3 'PenaltySurchargePercent'`).
- Condition: no element defined for late payment carries the late-delivery penalty rate.
- Options: (a, preferred) keep the penalty in the note only; (b) `PaymentPercent` ("The part of a
  payment, expressed as a percent, relevant for these payment terms") read as the share of the
  freight forfeited per day, which fits less well; (c) leave the rule to the framework contract.
- Needs decision: no

### ore/03#F6 · Medium · The plan does not say what is to be carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- Why: the TEP is the agreed transport service; its consignment has only an ID, a weight and the
  two parties, no description or classification of the goods and no number of wagons, and the
  request it confirms has none either (`02-TransportExecutionPlanRequest.xml`). A reference
  `FRC-WAGON-LIST-11` suggests a wagon list, but its content is not in the flow.
- Condition: the plan states the goods to be carried (description or commodity code and quantity,
  and the wagons if the plan assigns them).
- Options: (a, preferred) a `cbc:SummaryDescription` of the consignment, as in the corrected
  request; (b) goods items and the planned wagons as transport equipment.
- Needs decision: no

### ore/03#F7 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/03#F8 · Low · Post-event duration on a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- Why: PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given
  event and the issuance of a notification". A pre-arrival notice is issued before the event; a
  notice one hour after arrival is a different notification (arrival report), which neither the
  type code nor the remarks mention.
- Condition: the requirement carries only the durations its notification type uses, or a second
  requirement describes the post-arrival notice.
- Options: (a, preferred) drop the post-event duration; (b) add a separate arrival notification
  requirement if the story needs it.
- Needs decision: no

### ore/03#F9 · Low · Locations named after companies
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Valdara Industries`
- Why: a location's name designates the place. The places are the mine siding (UN/LOCODE `XUSRV`)
  and the factory siding (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]`
  = `Ore from the mine siding to the factory siding, per tonne.`). The AtLocation ("location of a
  transport service … that does not require transport movement") names the carrier, and no
  stationary service of the plan takes place at the carrier (see F3).
- Condition: every location name designates a place; the AtLocation is the place of a stationary
  service of the plan, or is absent.
- Options: (a, preferred) siding names (and `XUSRV`) for from/at; factory siding for to; drop the
  notification location or name the place where the notice is received; (b) keep names and add IDs.
- Needs decision: no

### ore/03#F10 · Low · Waiting-time charge without currency and implausibly small
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- Why: the note gives no currency or unit of what is waiting (train, wagon). Read as 40 XUF per hour
  for the train, it is against a freight of 962 XUF per tonne, 1 720 441 XUF for the train
  (`06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`), about 0.002 % of the
  freight per hour, too little to be a charge worth agreeing. Per wagon (30 wagons) it is 1 200 XUF
  per hour, still small but possible.
- Condition: the waiting-time charge states currency and basis (per train or per wagon), in a
  magnitude that fits the freight.
- Options: (a, preferred) an amount with currency and basis (e.g. per train per hour) in a magnitude fitting the freight, with the
  basis stated; (b) refer to the framework contract's tariff.
- Needs decision: no

### ore/03#F11 · Low · Contacts do not fit the roles
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver is the transport user that accepts the plan; a sales customer-service officer
  of Valdara does not book inbound ore. The consignor's contact is where the carrier arranges
  loading; Serravona's sales office is the commercial desk.
- Condition: the receiver's contact handles transport for Valdara; the consignor's contact handles
  loading at the mine.
- Options: (a, preferred) role-specific contacts; (b) drop job title and department.
- Needs decision: no

### ore/03#F12 · Low · Buyer's logistics service provider copied into the plan
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics has no part in this transport (the consignee unloads itself). Master data
  without use (section 4.8); 75 `*.xml` files carry it.
- Condition: no service provider without a role in the plan.
- Options: (a, preferred) leave it out; (b) give it a role.
- Needs decision: no

### ore/03#F13 · Low · Wagon list referenced by ID only
- XPath: `/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`
- Why: the reference has no type code or description and the document is not in the flow; the
  receiver learns only from the ID that it may be a wagon list, and nothing says whether it lists
  the 30 wagons of this train.
- Condition: the reference says what kind of document it is.
- Options: (a, preferred) add `DocumentTypeCode`/`DocumentDescription`; (b) list the wagons in the
  plan instead (see F6).
- Needs decision: no

## Checked and consistent
- Request reference `VI-TR-26-0305` resolves to `02-TransportExecutionPlanRequest.xml`; standing plan
  `FRC-TEP-26-0001`, service description `FRC-TSD-26` and framework contract `VI-FRC-FW-2026` are the
  same as in the request.
- Issued 4 March 12:50, within the provider's response deadline (4 March); validity 4–13 March covers
  the service period 10–13 March.
- Consignment ID, weight (1 800 000 kg) and parties are the same as in the request; FCA agrees with
  `01-Order.xml`.
- Emissions, physics: 1.9 t CO2e for 1 800 t is 1.06 kg CO2e per tonne; at 20–30 g CO2e per
  tonne-km for diesel rail freight (own knowledge) that is about 35–50 km, plausible for two places
  in the same province. The distance itself is in no document of the flow.
- Bonus terms (2 % for delivery on the first day of the window) and the waiting time beyond two
  hours agree with the provider's remarks and special terms.
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-03-05`:
  suspected a user response deadline on a plan that is already confirmed — refuted because in the
  TEP exchange the transport user still accepts or rejects the provider's plan; a deadline for that
  acceptance fits.
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected copied
  text — refuted because TransportUserRemarks are the user's remarks, which the plan repeats from the
  request by design.
