# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/03-TransportExecutionPlan.xml`, Git blob `b9cd241a833ef55a0d6d59ac19ae0579457b6de6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
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
  TransportServiceCode list, which also has `RAILWAGON` ("A whole wagon for one consignment"). The
  plan itself references a wagon list
  (`/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`); the ore is
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`),
  the despatch is
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`)
  and the carrier's own invoice for this plan bills
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`).
  The request 02 has the same code (ore/02#F1).
- Condition: the planned main service describes bulk carriage in rail wagons, consistent with 01, 02,
  04, 06 and the wagon list.
- Options: (a, preferred) `RAILWAGON` with a matching name; (b) a new world code for a whole (block)
  train.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### ore/03#F2 · High · Pre-arrival notification period lies before the transport
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:EndDate` = `2026-03-08`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: NotificationPeriod is "A period during which a notification will be issued". The notice is a
  pre-arrival notice two hours before arrival (also
  `/TransportExecutionPlan/cbc:TransportServiceProviderRemarks` = `Collection as requested; notice two hours before arrival.`).
  The service starts on 2026-03-10 and ends by 2026-03-13 (`ServiceEndTimePeriod`), and the waybill
  is issued 2026-03-10 11:35 (`05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`), so the notice
  can only be issued between 10 and 13 March, never from 4 to 8 March.
- Condition: the notification period lies within the possible arrival times (the service window
  2026-03-10 to 2026-03-13), or is left out.
- Options: (a, preferred) 2026-03-10 to 2026-03-13; (b) remove the period, since the two-hour lead
  time already fixes when the notice is issued.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F3)

### ore/03#F3 · High · Plan confirmed "as requested" but differs from the request
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusCode` = `Confirmed`
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonDescription` = `Capacity available on the requested day.`
- XPath: `/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `WEIGH`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`
- Why: `ASREQUESTED` means "Confirmed as the request asked" (the world's list also has `CHANGED`
  "Confirmed, but not as requested"). Yet the plan drops the weighing service the request asked for
  (with tariff class B), adds a pre-arrival notice, moves the place of the stationary service from
  the mine siding to "Ferrano Rail Cargo", and shows other "transport user special terms" than the
  user specified. TransportUserSpecialTerms is "Text describing special terms specified by the
  transport user": the user did not specify the text the plan attributes to it. The reason text
  speaks of "the requested day", while the request asked for a window (10–13 March). The weighed
  quantity of 1 788.4 t in 04/05 suggests the weighing took place. The confirmation contradicts the
  referenced request.
- Condition: the status reason agrees with the content: if the plan is as requested, it contains the
  requested weighing service at the mine siding and the user's special terms of 02 (the provider's
  own additions as provider terms or remarks), and the reason text refers to the requested window;
  if it differs, the reason is `CHANGED` and the reason description or provider remarks say what
  changed.
- Options: (a, preferred) keep `ASREQUESTED`, carry over `WEIGH`, the AtLocation and the user's
  sheeting term from 02, and put the notice and the slot/unloading terms on the provider's side,
  because 04/05 show a weighed quantity; (b) `CHANGED` with a description of the changes.
- Needs decision: yes (whether the weighing at the siding is part of the agreed service changes the
  story; context part)
- From: broad (F3), logistics (F3, as Medium), context (F2), parties (F5, the AtLocation change)

### ore/03#F4 · High · Freight payment terms contradict the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `06-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-11`
- Why: the plan agrees payment 30 days net from the consignment note; the consignment note is dated
  2026-03-10 (`05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`), so payment is due on
  2026-04-09. The carrier's invoice for this transport (it references this plan) counts 30 days from
  its own date (2026-03-12 → 2026-04-11) and offers a 2 % settlement discount the plan does not
  have. The two documents describe the same freight payment differently; the money part noted it as
  a problem of 06, but a contradiction with another example describing the same object is a finding
  here as well (section 4).
- Condition: the plan's payment terms and the freight invoice's terms, due date and discount agree.
- Options: (a, preferred) align the invoice with the plan (due 2026-04-09, no discount), since the plan
  is the agreed term; (b) state in the plan the terms the invoice applies.
- Needs decision: no
- From: broad (F4); money ("Checked and consistent": recorded for 06)

### ore/03#F5 · Medium · Late-payment surcharge element used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PenaltySurchargePercent is "The penalty for payment after the settlement period, expressed as
  a percentage of the payment", a surcharge the debtor owes for paying late. Here it carries the
  carrier's penalty for delivering late. The aggregate PenaltyPaymentTerms ("Terms of payment
  applying to a penalty specified in the transport execution plan") fits; the element inside it does
  not: it states a late-payment surcharge nobody agreed, and loses the per-day basis and the 25 %
  cap. The same note and element occur in 3 `*.xml` files (rail/03, plastics/04 and this one;
  `grep -rl --include='*.xml' '5 % of the freight per day late'`).
- Condition: no element defined for late payment carries the late-delivery penalty rate; the penalty
  (5 % per day, at most 25 %) is still stated in PenaltyPaymentTerms.
- Options: (a, preferred) keep the penalty in the note only and drop PenaltySurchargePercent, since
  UBL 2.5 has no structured element for a per-day delivery penalty (possibly a finding for the TC);
  (b) if a late-payment surcharge for the freight is wanted, state it in the freight PaymentTerms.
- Needs decision: no
- From: broad (F5), money (F1), context (F4)

### ore/03#F6 · Medium · The plan does not say what is to be carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- Why: the Transport Execution Plan is the agreement on the transport service; its consignment
  holds only an ID, a weight and the parties: no goods item, description, commodity code or number
  of wagons. That the goods are bulk iron ore appears only in the free-text note, and the wagons
  only in an external wagon list. The request it confirms has the same gap (ore/02#F2).
- Condition: the consignment states in structured form what is carried (goods item with description
  and/or HS `260111`, quantity) and, if the plan agrees the wagons, their number.
- Options: (a, preferred) a goods item with the values of 01; optionally the planned wagons as
  transport equipment; (b) at least a consignment-level description.
- Needs decision: no
- From: broad (F6), context (F6), logistics (F8, as Low)

### ore/03#F7 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this
  address is located"; a province belongs in `CountrySubentity`, as the world does for Bayvarra's
  states. 219 occurrences in 104 `*.xml` files (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`, or the world states why an
  Urvanian province is a region.
- Options: (a, preferred) move to `CountrySubentity` in all Urvanian addresses; (b) record a decision
  if deliberate; (c) drop.
- Needs decision: no
- From: broad (F7), parties (F1), logistics (F5, the location addresses), context (F7)

### ore/03#F8 · Medium · AtLocation names the carrier, and no stationary service is planned
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does
  not require transport movement". The plan's only additional service is the pre-arrival notice,
  which has no place, and "Ferrano Rail Cargo" is a company, not a place. The element has no content
  in its own meaning here (the change from the request is part of F3).
- Condition: AtLocation is present only for a stationary service of this plan and names that
  service's place.
- Options: (a, preferred) "Serravona mine siding" together with the restored weighing service (F3
  option a); (b) remove AtLocation.
- Needs decision: no
- From: context (F5), logistics (F6, as Low), parties (F5, as Low), broad (F9)

### ore/03#F9 · Medium · Post-event duration on a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given
  event and the issuance of a notification", PreEventNotificationDurationMeasure "the length of time
  to elapse between the issuance of a notification and the occurrence of the event it relates to".
  One notification of type `PREARRIVAL` ("Notice before the means of transport arrives") cannot be
  issued both two hours before and one hour after the arrival; no text in the plan mentions a
  notice after arrival.
- Condition: the requirement for the pre-arrival notice carries only the pre-event duration; a
  notice after arrival, if wanted, is a requirement of its own type.
- Options: (a, preferred) remove the post-event duration; (b) add a second requirement (arrival
  confirmation) with the one-hour post-event duration, if the story needs it.
- Needs decision: no
- From: logistics (F4), broad (F8, as Low), context (F9, as Low)

### ore/03#F10 · Low · Locations named after companies, not places
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Valdara Industries`
- Why: Location/Name is "The name of this location". The origin and destination are the mine siding
  (`/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:ID` =
  `XUSRV`) and the factory siding
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Ore from the mine siding to the factory siding, per tonne.`);
  the locations carry the company names and their BUSINESS addresses instead. NotificationLocation is
  "A location at which a notification will be issued": the carrier issues the notice from the train
  or its control office, and "Valdara Industries" is the notified party, already in NotifyParty.
- Condition: FromLocation and ToLocation name and identify the two sidings; the notification location
  is the place where the notice is issued, or is left out.
- Options: (a, preferred) siding names (with `XUSRV` for the mine), and no NotificationLocation;
  (b) keep company names with the sidings as `SubsidiaryLocation` or identifiers.
- Needs decision: no
- From: broad (F9), parties (F4), logistics (F7), context (F8, and F9 for the notification location)

### ore/03#F11 · Low · Waiting-time charge without currency, implausibly small, in a payment-terms element
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportServiceProviderSpecialTerms` = `Waiting time beyond two hours is charged.`
- Why: ServiceChargePaymentTerms is "Payment terms for the service charge associated with the
  transport service"; the note gives the rate, not when or how it is paid, without currency or basis
  (train or wagon). Against the freight (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount`
  = `962` XUF per tonne; `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` =
  `1720441`) 40 XUF per hour for the train is about 0.002 % of the freight per hour; per wagon
  (× 30) 1 200 XUF, still small. The same note occurs in 3 `*.xml` files (rail/03, plastics/04,
  ore/03; `grep -rl --include='*.xml' 'Waiting time 40 per hour'`), so it looks like a shared default.
- Condition: the waiting-time rate states currency and basis in a magnitude that fits the freight,
  and the element that carries it fits its definition.
- Options: (a, preferred) state the rate with currency and basis and how it is paid (e.g. "XUF … per
  train-hour beyond two hours, invoiced with the freight"); (b) move the rate to the provider's
  special terms, or refer to the framework contract's tariff.
- Needs decision: no
- From: broad (F10), money (F2)

### ore/03#F12 · Low · The transport user's and consignor's contacts are sales desks
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver is the transport user, which must accept the plan by its
  `TransportUserResponseRequiredPeriod`; its contact is transport planning, not the sales order desk.
  The consignor's contact is where the carrier arranges loading at the siding, not the sales office.
  Same contacts in every role of the flow (75 `*.xml` files with `order@valdara.example`).
- Condition: the receiver's contact books and accepts transport; the consignor's contact handles
  loading (or each is left out).
- Options: (a, preferred) role-specific contacts; (b) omit contacts or job title and department.
- Needs decision: no
- From: broad (F11), parties (F2), context (F10)

### ore/03#F13 · Low · Party master data the plan does nothing with
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: section 4.8 and IND5. Castrano Logistics has no part in this transport (the consignee unloads
  itself) and occurs in no role in the flow; the share listing has no use in a transport plan; the
  road-access condition does not concern a rail collection at the siding. Service provider and ISIN
  each in 75 `*.xml` files.
- Condition: every aggregate of the parties has a use in this plan.
- Options: (a, preferred) leave them out (keep the PhysicalLocation's UN/LOCODE, or move it to
  FromLocation, F10); (b) give Castrano a role.
- Needs decision: no
- From: broad (F12: service provider), parties (F3), context (F11)

### ore/03#F14 · Low · Wagon list referenced by ID only
- XPath: `/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`
- Why: the reference has no type code or description, and the document is not in the flow
  (`flow_index.py ore`: `-> ?`); that it lists the wagons of this train is guessed from the number.
  It is the only evidence in the plan that wagons, not containers, are used (F1).
- Condition: the reference states its kind (DocumentTypeCode and/or DocumentType).
- Options: (a, preferred) a DocumentTypeCode from the world's list and DocumentType "Wagon list";
  (b) list the wagons in the plan as transport equipment instead (F6).
- Needs decision: no
- From: broad (F13), logistics (F8), context (F12)

### ore/03#F15 · Low · Standing plan and service description referenced but not in the flow
- XPath: `/TransportExecutionPlan/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
- XPath: `/TransportExecutionPlan/cac:TransportServiceDescriptionDocumentReference/cbc:ID` = `FRC-TSD-26`
- Why: neither resolves to an example (`flow_index.py ore`: `-> ?`). Both elements name their kind,
  the values are the same as in the request, and the documents may exist outside the examples
  (broad and context accepted them); whether they should be examples is a story question.
- Condition: each referenced document exists in the world as intended, or a decision records that it
  needs no example.
- Options: (a, preferred) record that they are documents outside the examples; (b) add them.
- Needs decision: yes
- From: logistics (F8)

## Checked and consistent
- Request reference `VI-TR-26-0305` resolves to 02 (a request, the right kind); standing plan,
  service description and framework contract `VI-FRC-FW-2026` (with ContractType "Framework transport
  agreement") are the ones of 02; consignment ID, weight 1 800 000 kg, parties, service window and
  FCA agree with 02 and 01.
- Dates: issued 2026-03-04 12:50, within the provider's response deadline 2026-03-04; validity
  2026-03-04 to 2026-03-13 covers the service window; user response by 2026-03-05, after the issue.
- Roles: sender, service provider and signatory Ferrano Rail Cargo; receiver, transport user,
  bill-to, notify party and consignee Valdara; consignor Serravona; as in 02, reversed for the answer.
  Bill-to Valdara agrees with FCA and with the customer of 06.
- Emissions: 1.9 t CO2e for 1 800 t is 1.06 kg CO2e per tonne; at 15–30 g CO2e per tonne-km for
  diesel rail freight (own knowledge, GLEC order of magnitude) that is about 35–70 km, plausible for
  two places in one province; the distance itself is in no example.
- Bonus (2 % for delivery on the first day of the window, 2026-03-10) and penalty (5 % per day, capped
  at 25 %, i.e. five days) are coherent rules in themselves; the waiting time beyond two hours agrees
  with the provider's special terms.
- Party descriptions identical in all eight ore examples; ISIN check digit correct.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-03-05`:
  suspected a user deadline on a plan already confirmed — refuted because in the TEP choreography the
  user still accepts or rejects the provider's plan. (from broad, logistics, context)
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: suspected the
  provider writing the user's remarks — refuted because it repeats the user's remark from 02, as the
  element allows. (from broad, logistics, context)
- `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000` against the actual
  1 788.4 t — refuted: the plan states the planned weight before loading. (from logistics)
- `/TransportExecutionPlan/cac:TransportServiceProviderResponseRequiredPeriod/cbc:EndDate` =
  `2026-03-04`: the provider's own deadline in its plan — refuted because the plan records the
  deadline it answers, the value of 02. (from context)
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:DeliveryTerms/cbc:ID` = `FCA`: Incoterms in
  a transport contract — refuted because the sale is FCA, which is why the buyer contracts the
  carriage. (from context)
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note`: a bonus
  without business reason — refuted, the note gives it. (from context) Also suspected that the bonus
  condition can never be met because the order's window starts on
  `01-Order.xml:/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09` — refuted
  because the window the plan agrees is its own service window, whose first day (2026-03-10) is
  reachable on a short run. (from money)
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note`: cap of 25 %
  against the window — coherent, no inconsistency. (from money)
- English renderings in Italian form, `+999` telephone numbers, ISO 6523 ICD `0990`, Ferrano Rail
  Cargo `SMALL`: refuted as in 01 (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined.
- broad/F2, logistics/F2, context/F3 → F2: combined, type code added as evidence.
- broad/F3, logistics/F3, context/F2, parties/F5 (AtLocation change) → F3: combined; severity High
  (logistics: Medium) because the status reason contradicts the referenced request; Needs decision
  yes taken from context.
- broad/F4 → F4: kept as a finding of this example, although the money part assigned it to 06 only,
  because section 4 makes a contradiction with another example describing the same object a finding
  of both.
- broad/F5, money/F1, context/F4 → F5: combined.
- broad/F6, context/F6, logistics/F8 (goods part) → F6: combined; Medium (logistics: Low), as in
  ore/02#F2.
- broad/F7, parties/F1, logistics/F5, context/F7 → F7: combined; Needs decision no (parties: yes), as in
  ore/01#F1.
- context/F5, logistics/F6, parties/F5, broad/F9 (AtLocation) → F8: severity Medium (logistics and
  parties: Low), because the element carries no service place at all, a meaning other than its
  definition; the difference from the request is in F3.
- logistics/F4, broad/F8, context/F9 (post-event part) → F9: severity Medium (broad and context: Low),
  because the value cannot apply to the notification type it is given for; the notification location
  of context/F9 moved to F10.
- broad/F9, parties/F4, logistics/F7, context/F8 and the notification location of context/F9 → F10.
- broad/F10, money/F2 → F11: combined; money's point about the element's definition added.
- broad/F11, parties/F2, context/F10 → F12; broad/F12, parties/F3, context/F11 → F13: combined.
- broad/F13, context/F12, logistics/F8 (wagon-list part) → F14; logistics/F8 (standing plan and
  service description) → F15: split off, because it alone needs a decision.

## Outside this review
- Whether 30 wagons are available on 2026-03-10 and the route from Serravona to Ferrano exists on
  the map (capacity, route) is for the consistency review. (from logistics)
