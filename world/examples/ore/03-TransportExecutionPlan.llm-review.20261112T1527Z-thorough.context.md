# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

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

### ore/03#F1 · High · The plan confirms a container train for ore loose in wagons
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: RAILCONT is "Containers on a scheduled container train" in the world's TransportServiceCode list. The plan itself references a wagon list (`/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`), the ore is "loose in rail wagons" (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`), the despatch is 30 wagons (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`) and the carrier invoices "ore in bulk wagons" (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`). The list has RAILWAGON ("A whole wagon for one consignment"). The request 02 has the same code (see its review).
- Condition: the main transportation service describes bulk carriage in rail wagons, consistent with 01, 04, 06 and the wagon list.
- Options: (a) preferred: RAILWAGON, or a new code for a whole (block) train if that distinction is wanted; (b) none that keeps RAILCONT without contradicting four examples.
- Needs decision: no

### ore/03#F2 · High · "Confirmed as requested", but the plan differs from the request
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusCode` = `Confirmed`
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`
- XPath: `/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`
- Why: ASREQUESTED means "Confirmed as the request asked" (world list DocumentStatusReasonCode, which also has CHANGED "Confirmed, but not as requested"). The request asked for an additional weighing service at the mine siding (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `WEIGH`, `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`) and stated the user's special term "Wagons sheeted against dust." (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`). The plan drops the weighing, adds a pre-arrival notice, moves the AtLocation, and shows other "transport user special terms" than the user asked for. Either the confirmation is not "as requested", or the plan does not carry what was requested.
- Condition: the status reason agrees with the content: if the plan is as requested, it contains the requested weighing service (at the mine siding) and the user's special terms of 02; if it differs, the reason is CHANGED and the differences are what the carrier changed.
- Options: (a) preferred: keep ASREQUESTED and carry over WEIGH, the AtLocation and the user's term from 02 (the pre-arrival notice may be added as the carrier's own term), because 04/05 show a weighed quantity (1788.4 t), so the weighing took place; (b) CHANGED with a reason description that says what changed.
- Needs decision: yes (whether the weighing at the siding is part of the agreed service changes the story)

### ore/03#F3 · High · The pre-arrival notice period ends before the train can run
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:StartDate` = `2026-03-04`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationPeriod/cbc:EndDate` = `2026-03-08`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: NotificationPeriod is "a period during which a notification will be issued". The notification is a pre-arrival notice issued 2 hours before the arrival (also `/TransportExecutionPlan/cbc:TransportServiceProviderRemarks` = `Collection as requested; notice two hours before arrival.`), and the service starts on 2026-03-10 and ends by 2026-03-13; the notice can therefore only be issued between 2026-03-10 and 2026-03-13, not from 4 to 8 March.
- Condition: the notification period lies within the service period (or is omitted, since the 2-hour lead time already fixes when the notice is given).
- Options: (a) preferred: NotificationPeriod 2026-03-10 to 2026-03-13; (b) leave NotificationPeriod out.
- Needs decision: no

### ore/03#F4 · Medium · A late-payment element carries the penalty for late delivery
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- Why: PenaltySurchargePercent is "the penalty for payment after the settlement period, expressed as a percentage of the payment". The penalty here is the carrier's for late delivery of the train (`/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`), i.e. a delivery penalty, not a late-payment surcharge; PenaltyPaymentTerms as such ("terms of payment applying to a penalty specified in the transport execution plan") fits, the percent element does not. The same note and element occur in 3 XML examples (`grep -rl --include='*.xml' '5 % of the freight per day late' world/examples`).
- Condition: no late-payment element is used for the delivery penalty; the 5 % per day and the 25 % cap are stated where UBL defines a penalty for late performance, or only in the note.
- Options: (a) preferred: keep the note only (UBL 2.5 has no structured element for a delivery-delay penalty percentage in PaymentTerms); (b) record it as a finding for the TC if a structured element is wanted.
- Needs decision: no

### ore/03#F5 · Medium · AtLocation names the carrier, and no service without movement is planned
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "the location of a transport service (e.g., terminal handling service) that does not require transport movement". The only additional service in the plan is a pre-arrival notice, which has no location; and "Ferrano Rail Cargo" is a company, not a place. The element has no content in its own meaning here (see F2 for the difference with 02).
- Condition: AtLocation is present only for a stationary service of this plan and names that service's place.
- Options: (a) preferred: the mine siding together with the weighing service (F2 option a); (b) leave AtLocation out if there is no stationary service.
- Needs decision: no

### ore/03#F6 · Medium · The plan does not say what is carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- Why: the Transport Execution Plan is the agreement on the transport service; the consignment holds only an ID, a weight and the parties, no goods item, description or commodity code. That the goods are bulk iron ore (dust, wagon type, tariff) appears only in the free-text note.
- Condition: the consignment states in structured form what is carried (goods item with description and/or commodity classification, quantity).
- Options: (a) preferred: a goods item with the values of 01 (iron ore lump, HS 260111, 1800 t); (b) at least a goods description in the consignment.
- Needs decision: no

### ore/03#F7 · Medium · A province is given in `Region`
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" and belongs in `CountrySubentity`, as for Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it to `CountrySubentity`; (b) rename it if it is an economic region.
- Needs decision: no

### ore/03#F8 · Low · From- and to-location are company names with office addresses
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: the origin and destination are the mine siding and the factory siding (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Ore from the mine siding to the factory siding, per tonne.`); the locations carry the company names and their BUSINESS addresses instead. The mine has UN/LOCODE `XUSRV` in the consignor's PhysicalLocation.
- Condition: FromLocation and ToLocation name and identify the two sidings.
- Options: (a) preferred: siding names with identifiers (XUSRV for the mine); (b) keep addresses but with place names.
- Needs decision: no

### ore/03#F9 · Low · Notification details that do not fit a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Valdara Industries`
- Why: the requirement is a PREARRIVAL notice ("Notice before the means of transport arrives"), with a lead time of 2 hours. A PostEventNotificationDurationMeasure ("the length of time between the occurrence of a given event and the issuance of a notification") of 1 hour has no meaning for a notice that precedes the event, and nothing in the plan describes a second, after-the-event notice. NotificationLocation is "a location at which a notification will be issued"; the carrier issues it (from the train or its operations), and "Valdara Industries" is the notified party's name, already given in NotifyParty.
- Condition: the notification requirement carries only values that belong to a pre-arrival notice; a location, if any, is a place.
- Options: (a) preferred: drop PostEventNotificationDurationMeasure and NotificationLocation; (b) if an arrival confirmation one hour after arrival is meant, model it as its own requirement with a fitting type.
- Needs decision: no

### ore/03#F10 · Low · The transport user's and consignor's contacts are sales desks
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- Why: the receiver of the plan is the transport user, whose contact must accept the plan and coordinate the train; the consignor's contact hands over the goods. Both are customer-service desks in Sales, copied from master data.
- Condition: the contacts are functions that handle the transport and the loading.
- Options: (a) preferred: logistics/inbound contact for Valdara, siding/loading contact for Serravona; (b) omit.
- Needs decision: no

### ore/03#F11 · Low · Party master data the plan does nothing with
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the share listing and the warehousing provider (in no role in the flow) have no use in a transport plan; the road-access condition does not concern a rail collection at the siding. Same master data in 75 XML examples each (SecurityListing `XU0001042501`, provider `VI-SP-2026-01`).
- Condition: every aggregate of the parties has a use in this plan.
- Options: (a) preferred: leave them out (keep the PhysicalLocation's UN/LOCODE, or move it to FromLocation, F8).
- Needs decision: no

### ore/03#F12 · Low · The wagon-list reference does not say what it is
- XPath: `/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WAGON-LIST-11`
- Why: the reference has only an ID; that it is the list of wagons allocated to the train is guessed from the number. It matters for F1 (it is the evidence that wagons, not containers, are used).
- Condition: the reference states its kind (DocumentTypeCode and/or DocumentType).
- Options: (a) preferred: add a DocumentTypeCode from the world's document-type list and a DocumentType "Wagon list"; (b) carry the wagons as TransportEquipment/TransportMeans instead, if the plan should name them.
- Needs decision: no

## Checked and consistent
- References: `VI-TR-26-0305` resolves to 02 (a request, the right kind); contract `VI-FRC-FW-2026` is the one of 02, here with its type "Framework transport agreement"; consignment `VI-CS-26-0306` and its weight 1 800 000 kg agree with 02.
- Dates: issued 2026-03-04 12:50, within the provider's response deadline 2026-03-04 of 02; validity 2026-03-04 to 2026-03-13 covers the service window 2026-03-10 to 2026-03-13 of 02.
- Parties: sender/service provider Ferrano Rail Cargo, receiver/user/bill-to Valdara, as in 02 reversed.
- Emission estimate (`/TransportExecutionPlan/cac:TransportExecutionTerms/cac:EnvironmentalEmission/cbc:ValueMeasure` = `1.9`) for 1800 t: 1.06 kg CO2e per tonne, which at a typical 20–30 g CO2e/tkm for rail freight (own knowledge) means about 35–55 km, a plausible distance between mine and works in one province.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportServiceProviderResponseRequiredPeriod/cbc:EndDate` = `2026-03-04`: the provider's own response deadline in the provider's plan — refuted because the TEP model carries it to record the deadline the plan answers, and the value is the one of 02.
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-03-05`: a user response deadline for a plan already "confirmed" — refuted because in the TEP choreography the user still accepts the provider's plan; the deadline is meaningful.
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:DeliveryTerms/cbc:ID` = `FCA`: Incoterms in a transport contract — refuted because the buyer contracts the carriage precisely because the sale is FCA; the delivery terms explain who pays the freight.
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: user remarks in the provider's document — refuted because the element is defined for the user's remarks "regarding the transport operations referred to in the Transport Execution Plan" and repeats those of 02.
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note` = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`: a bonus without a business reason — refuted, the note gives the reason.
