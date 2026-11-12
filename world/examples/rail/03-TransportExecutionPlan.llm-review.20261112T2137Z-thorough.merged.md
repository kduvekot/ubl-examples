# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/03-TransportExecutionPlan.xml`, Git blob `10a1218954b5cf3553a1e440bbc205476072297d` (committed)
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

### rail/03#F1 · High · Main service "Full truck load" contradicts the plan's container train
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `/TransportExecutionPlan/cac:MainTransportationService/cbc:Name` = `Full truck load`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:TransportMeansTypeCode` = `2302`
- Why: FTL is "One truck for one consignment, from the place of loading to the place of delivery" (world TransportServiceCode list, checked in `world/codelists/lists.json`). The plan confirms carriage of two 40-foot containers by rail (mode 2, transport means type 2302 "Train, container", train FRC 4417), and the goods item itinerary whose segment is governed by this plan says RAILCONT, "Containers on a scheduled container train": `09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cbc:TransportExecutionPlanReferenceID` = `FRC-TEP-26-0328` with `09-GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cac:TransportationService/cbc:TransportServiceCode` = `RAILCONT`. The truck leg is only the carrier haulage the Note describes. Merge check (refutation attempted): reading FTL as a description of the truck leg alone fails, because the definition runs "from the place of loading to the place of delivery" and the delivery is at Marrowdale by rail. The same contradiction is in the request (rail/02 F1).
- Condition: MainTransportationService describes the rail main carriage and agrees with the itinerary; the road leg, if stated, is an additional service or a pre-carriage stage.
- Options: (a) preferred: RAILCONT as main service, the road leg as a `cac:PreCarriageShipmentStage` (mode 3) carrying the planned pickup, or as AdditionalTransportationService (CARRHAUL's list text speaks of a port and a shipping line, so it would need widening); (b) RAILWAGON if a whole wagon is meant; (c) restrict the plan to the truck leg and plan the rail transport separately (changes the flow: the waybill, itinerary and invoice refer to this plan for the rail part).
- Needs decision: no
- From: broad (F3), context (F2), logistics (F1, first part)

### rail/03#F2 · High · Planned pickup lies before the period in which the service must begin
- XPath: `/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-04-14`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: ServiceStartTimePeriod is "the period within which the service must begin". The provider plans to collect the containers at Castrano on 13 April 15:00 ("Collection as requested"), a day before the period opens. The waybill confirms the actual pickup at that time (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cbc:ActualPickupDate` = `2026-04-13`). The request has the same contradiction (rail/02 F2). Merge check: confirmed; the pickup is an event of the consignment this plan carries, so it is part of the service.
- Condition: every planned event of the service lies within or after ServiceStartTimePeriod.
- Options: (a) preferred: start the period on 2026-04-13 (request and plan); (b) plan the pickup on 14 April; (c) if the period is meant for the rail main carriage only, that follows from fixing F1/F3 with a pre-carriage stage whose start is stated separately.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F2)

### rail/03#F3 · High · ToLocation is the hub, but the plan delivers to the siding in Marrowdale
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:Description` = `Container slots between the Ferrano hub and Marrowdale.`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`
- Why: ToLocation is "The destination location for the transport service referenced in the Transport Execution Plan". The plan's main carriage is a rail stage ending in Marrowdale, where the containers are shunted to Lumeway's siding and delivered on 15 April 11:00, under a contract for slots "between the Ferrano hub and Marrowdale". The hub is where the containers change from road to rail, not the destination; the road leg to it has no pre-carriage stage.
- Condition: ToLocation is where the planned service ends (Lumeway's siding, Marrowdale), and From/To describe the same transport as the consignment's stages; or the plan covers only the leg its From/To describe.
- Options: (a) preferred: ToLocation = Lumeway's rail siding, Marrowdale (GLN 9520610900015 as on the waybill), the hub as a stage location, a pre-carriage stage for the road leg; (b) separate plans per leg (changes the flow).
- Needs decision: no
- From: broad (F2), context (F3), logistics (F1, second part)

### rail/03#F4 · High · Agreed payment terms contradict the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`
- XPath: `10-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-17`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- Why: TransportExecutionTerms/PaymentTerms are the payment terms agreed for the transport service. They run 30 days net from the consignment note, the waybill FRC-WB-26-0334 issued 2026-04-14, so the freight falls due on 2026-05-14. The freight invoice, which bills this service and references the waybill, is due on 2026-05-17 (30 days from its own issue date 2026-04-17) and grants a 2 % settlement discount within 10 days, which "net" excludes. Merge check (refutation attempted): a later due date could be read as the carrier being generous, but the invoice states different terms (basis date and discount) for the same freight, and "net" and a settlement discount cannot both hold; recomputed 14 April + 30 days = 14 May. The same plan note occurs in 3 files (`grep -rl --include='*.xml' '30 days net from the consignment note' world/examples | wc -l`: plastics/04, ore/03 and this one).
- Condition: the payment terms agreed in this plan and the due date, discount and basis date applied in `10-Invoice.xml` agree.
- Options: (a) preferred (money): state in the plan the terms the carrier actually bills (30 days from the invoice date, 2 % within 10 days), since the invoice terms are the carrier's standard terms; (b) keep "from the consignment note" and make the invoice due 2026-05-14 without a discount (broad's first variant); (c) explain a deviation in the invoice.
- Needs decision: no
- From: broad (F4), money (F1)

### rail/03#F5 · Medium · Province in Region of four Urvanian addresses
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division, which UBL puts in CountrySubentity, as the consignee's Bayvarran address in the same document does (`/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files.
- Condition: no Urvanian address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it; (c) keep Region with a stated world rule if provinces are not administrative.
- Needs decision: no
- From: broad (F8), context (F8), logistics (F4), parties (F1)

### rail/03#F6 · Medium · AtLocation names the carrier and no stationary service exists
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does not require transport movement". Its only content is the name of the transport service provider (`/TransportExecutionPlan/cac:TransportServiceProviderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`), a company, without address or identifier, and the plan has no stationary service (main service and a pre-arrival notice only).
- Condition: AtLocation is absent, or names the place (with address or identifier) of a stationary service the plan contains.
- Options: (a) preferred: drop it; (b) if terminal handling at the hub is part of the plan, add it as an AdditionalTransportationService and give the hub (UN/LOCODE XUFER) as AtLocation.
- Needs decision: no
- From: broad (F7), context (F4), logistics (F3), parties (F4)

### rail/03#F7 · Medium · Late-payment surcharge percent used for a per-day late penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:TimeBasisCode` = `ANN`
- Why: PenaltySurchargePercent is "The penalty for payment after the settlement period, expressed as a percentage of the payment", a single percentage of a late payment. The note describes 5 % of the freight for every day late, capped at 25 %. Read as a penalty on the carrier for late delivery (broad, context; the usual meaning of a percentage of the freight per day of delay in rail transport, own knowledge), the element carries a meaning other than its definition. Read as a penalty for late payment (money's alternative), 5 % per day contradicts the freight invoice's 8 % a year, simple interest. Either way the structured value does not express the note: the per-day basis and the cap are lost. Which penalty the agreement means is a story question. The same pair occurs in 3 files (plastics/04, ore/03, here).
- Condition: PenaltySurchargePercent is present only for a percentage of a payment made after the settlement period, and then agrees with the late-payment terms of `10-Invoice.xml`; a late-delivery penalty is not expressed in it.
- Options: (a) preferred, if the penalty is for late delivery: keep it in the Note only (PenaltyPaymentTerms, "terms of payment applying to a penalty specified in the transport execution plan", fits a penalty in general; no UBL element defines a delay-penalty percent), and say it is the carrier's liability for delay; (b) if it is for late payment: align with the invoice's 8 % a year and remove the per-day wording.
- Needs decision: yes
- From: broad (F6), context (F5), money (F2)

### rail/03#F8 · Medium · Language code in LocaleCode of the consignee
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en` and names no locale. 364 occurrences (recounted in the merge).
- Condition: LocaleCode is absent or a locale from a list of locales.
- Options: (a) preferred: drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F9), context (F7), parties (F2)

### rail/03#F9 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". "Gate 3" is a site entrance, not a street name; and the plan delivers by rail to the siding (`/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`), so the gate is not even the delivery point.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) preferred: remove it; (b) state access details, where needed, at a delivery location.
- Needs decision: no
- From: broad (F10), parties (F3)

### rail/03#F10 · Low · "English" renderings of Urvanian street names and legal forms are Italian
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via del Terminal`
- Why: Each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings next to them are different names. Whether the world keeps Italianate names as English usage for Urvania (broad's argument in rail/01 and rail/02) cannot be settled by the merge; for the legal forms, which are descriptions, it is the weaker argument. 217 such renderings in 102 files (count as in rail/01 F10).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) preferred: record the convention in the world's story and keep the values, if intended; (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F5)

### rail/03#F11 · Low · Registration date 1996-01-01 of the carrier
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A registration on New Year's Day reads as a placeholder (own knowledge of register practice); the same date occurs 271 times in 181 files for many different companies (`grep -rh --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`). No part of this run raised it for rail 01–05; the merge adds it for consistency with the wood, plastics, air and rail 06–11 merges.
- Condition: each company has its own registration date, or the story records an event that explains the shared date.
- Options: (a) preferred: an own date per company from its history; (b) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: merge

### rail/03#F12 · Low · Legal-entity master data the plan does nothing with
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: a transport plan does nothing with the transport user's stock-exchange listing or with the share capital of the transport user or the consignee.
- Condition: every legal-entity element present has a purpose in the plan.
- Options: (a) preferred: drop SecurityListing and CorporateStockAmount here; (b) a reduced party description for transport documents.
- Needs decision: no
- From: context (F12), parties (F9)

### rail/03#F13 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the plan as transport user and has to respond by `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-09`; that response and the arrangements for collection belong to its shipping or logistics function, not to the order desk that takes customer orders. The plan makes the consignee unload (`/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`) and counts free time at its siding, so the carrier needs Lumeway's goods-in or siding contact, not its sales customer service.
- Condition: the transport user's contact is a shipping/logistics function of Valdara, the consignee's contact Lumeway's goods-receiving function (or Contact is absent).
- Options: (a) preferred: role-specific contacts; (b) role-specific contacts in the parties' master data.
- Needs decision: no
- From: broad (F14, second part), parties (F6, F7)

### rail/03#F14 · Low · One framework contract under two identifiers
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:ID` = `VI-FRC-FW-2026`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:TransportContract/cbc:ID` = `FRC-CON-2026-005`
- Why: The document-level contract is a "Framework transport agreement" (version 2, ten more slots a month, call-off 88) whose contract document is FRC-CON-2026-005-A1, by its form amendment 1 of FRC-CON-2026-005. The consignment's contract is FRC-CON-2026-005, "Framework contract for container slots", and the waybill links call-off 88 to that number (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ContractedCarrierAssignedID` = `FRC-CON-2026-005/88`). The same contract thus appears under VI-FRC-FW-2026 and FRC-CON-2026-005; a reader cannot tell whether these are one contract or two.
- Condition: one contract has one identifier throughout the flow, or the two identifiers are evidently different contracts (e.g. the transport user's own reference given as such).
- Options: (a) preferred: FRC-CON-2026-005 as the contract ID at both levels (the carrier's numbering, used by the waybill), version 2 with the amendment as ContractDocumentReference; (b) if VI-FRC-FW-2026 is Valdara's own number, keep it only in the request and say so.
- Needs decision: no
- From: broad (F5), context (F9), logistics (F5)

### rail/03#F15 · Low · Nomination deadline and nomination period disagree; contract issue time without date
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:IssueTime` = `10:00:00`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationDate` = `2026-04-08`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cbc:NominationTime` = `09:00:00`
- XPath: `/TransportExecutionPlan/cac:TransportContract/cac:NominationPeriod/cbc:EndDate` = `2026-04-12`
- Why: NominationDate is "the deadline date by which the services … have to be booked" (8 April 09:00), while NominationPeriod, "the period required to book the services … before the services can begin", runs to 12 April: two different last booking moments. The contract's IssueTime 10:00 has no IssueDate, so it identifies no point in time (the consignment's copy of the contract has the date 2026-01-05 and no time).
- Condition: the nomination deadline and the nomination period agree (the deadline is the end of the period, or one is absent), and the contract's issue time comes with its date or is absent.
- Options: (a) preferred: keep the deadline 2026-04-08 09:00 (the request came before it) and end the period then, or drop the period; give IssueDate 2026-01-05 with the time, or drop the time; (b) keep the period and drop the deadline.
- Needs decision: no
- From: broad (F11), context (F10), logistics (F6)

### rail/03#F16 · Low · From location named after the company, not the place
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- Why: A location's name is the place, not the company. The waybill calls the same place `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`, so the place has two names in the flow, and no identifier links them.
- Condition: the origin location's name names the warehouse, the same way in every example of the flow.
- Options: (a) preferred: "Castrano Logistics warehouse, Ferrano" everywhere; (b) add a location identifier used wherever the warehouse occurs.
- Needs decision: no
- From: broad (F14, first part), parties (F8)

### rail/03#F17 · Low · Pre-arrival notification with a post-event duration
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given event and the issuance of a notification". A pre-arrival notice is issued before the arrival (two hours, as the provider's remarks say: "notice two hours before arrival"); a notice one hour after the event is a different notification that nothing in the plan describes.
- Condition: the requirement carries only the timing its type needs, or a second requirement of its own type states the post-event notice.
- Options: (a) preferred: drop the post-event duration; (b) a separate NotificationRequirement (e.g. arrival confirmation) with it.
- Needs decision: no
- From: broad (F12), context (F6), logistics (F8)

### rail/03#F18 · Low · Waiting-time charge without a currency, at an implausible rate
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`
- Why: The note gives a rate without a currency, so it cannot be applied; every amount of the flow is in XUF. Read as 40 XUF, an hour of waiting would cost 0.07 % of the freight for one container (40 / 54 600), not a plausible charge for a tractor or train crew (a bench costs 49 900 XUF in 01). The same note occurs in 3 files (plastics/04, ore/03, here).
- Condition: the waiting-time charge names its currency, at a level plausible against the carrier's freight rates.
- Options: (a) preferred: the rate with currency at a plausible level (e.g. a few thousand XUF per hour); (b) say only that waiting time is charged per the framework contract.
- Needs decision: no
- From: broad (F13, second part), money (F3)

### rail/03#F19 · Low · Planned and estimated events without locations
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:PlannedDeliveryTransportEvent/cbc:OccurrenceTime` = `11:00:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceTime` = `10:30:00`
- Why: None of the plan's events has a location. With From/To pointing to the warehouse and the hub (F3), the reader cannot tell that the departure at 06:45 is from the hub and the arrival at 10:30 in Marrowdale. The waybill gives the departure location (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`).
- Condition: each planned departure, arrival, pickup and delivery names its place, or the stage's loading and unloading places make it unambiguous.
- Options: (a) preferred: `cac:Location` (name and UN/LOCODE XUFER / XBMRW, the siding's GLN) on the events, as the waybill does; (b) LoadingPortLocation/UnloadingPortLocation on the stage.
- Needs decision: no
- From: logistics (F7)

### rail/03#F20 · Low · Passenger quantity 0 on a freight train
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- Why: PassengerQuantity is "the total number of passengers aboard a transport means". A container train carries no passengers by its nature; stating 0 has no business reason (no fillers, nothing implied by absence: IND5/IND6). The same is in `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`; these are the only two occurrences (`grep -rh --include='*.xml' '<cbc:PassengerQuantity unitCode="IE">0<' world/examples | wc -l`).
- Condition: PassengerQuantity is absent unless the story gives a reason to state it.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F13, first part), context (F11), logistics (F9)

### rail/03#F21 · Low · Demurrage instructions for containers at a siding, under a definition about vessels
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions` = `Free time five days at the siding, then demurrage per container day.`
- Why: UBL defines DemurrageInstructions as "text of instructions relating to demurrage (the case in which a vessel is prevented from loading or discharging cargo within the stipulated laytime)". The value concerns container free time at a rail siding, which trade calls demurrage too. Context refuted it: demurrage of containers and wagons is the same concept in rail and intermodal practice, and the element is in a shipment stage of any mode. Whether the parenthesis restricts the element to vessels or only explains the term cannot be settled by the merge.
- Condition: the owner confirms that the parenthesis is only an explanation (and records it as a UBL definition question), or the container free time is stated elsewhere.
- Options: (a) preferred: keep it and record the definition question for the UBL TC; (b) move the text to TransportExecutionTerms/TransportServiceProviderSpecialTerms.
- Needs decision: yes
- From: logistics (F10); context listed it under "Considered and refuted"

## Checked and consistent
- Reference: `/TransportExecutionPlan/cac:TransportExecutionPlanRequestDocumentReference/cbc:ID` = `VI-TR-26-0326` resolves to rail/02, a request from the same transport user to the same provider; consignment ID, summary, weight 7968 kg, parties, remarks and notes agree; the plan answers before the requested deadline (2026-04-08; plan issued 16:46) (broad, context, logistics).
- Times against the issue time (2026-04-08 16:46): all planned and estimated events lie after it; user response deadline 2026-04-09 and validity 2026-04-08 to 2026-04-17 cover the service up to the service end 2026-04-17 (logistics, broad).
- Plan against request: departure 06:45 (requested 07:00), arrival 2026-04-15 10:30 (requested 15 April), delivery 2026-04-15 11:00 (requested 16 April, contractual latest 16 April): within what was asked, so "as requested" holds (broad, logistics, context).
- Planned and estimated times agree with 05 and 08 (06:45/06:50 departure, 10:30/10:40 arrival); train FRC 4417, journey CT 4471, loading sequence 7 and direction WB as in 08 (broad, logistics). Whether westbound is the direction from Ferrano to Marrowdale could not be checked from the examples (logistics).
- Transport means type 2302 (UNECE Rec. 28: train, container) fits mode 2 and the container consignment (logistics).
- BillToParty Valdara = AccountingCustomerParty of `10-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`; PrepaidPaymentTerms "Freight prepaid by the consignor under DAP" agrees with 08 and with the DAP of 01 (money, broad, context, parties).
- TransportServiceProviderSpecialTerms ("Waiting time beyond two hours is charged.") and ServiceChargePaymentTerms describe the same charge; ChangeConditions conflicts with no charge billed in the flow (money).
- Tax registrations of Valdara, Ferrano Rail Cargo and Lumeway are the same in every example of the flow (money).
- Roles agree with the request, sender and receiver swapped as a reply should be; full party descriptions identical to the other examples; FromLocation and ToLocation addresses identical to the request, the ToLocation address is the hub's postal address in 04 (parties).
- The notified party Ferrano Intermodal Hub has the same register ID `XU-R-105096` as in 04, 05 and 07; the pre-arrival notification agrees with the additional service NOTIFY and the provider remarks (parties, context).

## Considered and refuted
- `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`: departure (06:45 instead of 07:00) and delivery (15 instead of 16 April) differ from the request — refuted because both are within the requested windows (broad, logistics).
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-09`: pointless with status Confirmed — refuted because a confirmed plan may still need the user's acceptance (broad).
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:50:00`: an estimate in the plan itself, six days ahead — refuted because a plan may carry the provider's forecast next to the timetable; five minutes' difference is plausible (broad, context).
- `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01` (Castrano Logistics): master data copied — refuted because Castrano's warehouse is the collection place (FromLocation) (broad, parties).
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotifyParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: wrong party for a pre-arrival notice (the consignee unloads at Marrowdale) — refuted because the remark and the haulage note make the tractor's arrival at the hub a legitimate subject, and the notification location is the hub (broad, parties); logistics adds that after F3 is fixed the fixing session should check whom the notice goes to.
- `/TransportExecutionPlan/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note`: "prepaid" freight while invoiced afterwards on 30 days — refuted because "prepaid" is the freight term (paid by the consignor at origin), not payment in advance (money).
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:DemurrageInstructions`: demurrage per container day without a rate — refuted because the element holds instructions; the rate belongs to the framework contract and no demurrage is billed (money). Context's refutation of the vessel-definition question is given in F21, which the merge keeps as a finding (logistics).
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`: copied text — refuted because the plan repeats the user's remarks by definition (context).
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `CT 4471` against `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`: transposed digits — refuted: different identifiers (schedule, train), used consistently in 04, 05, 08 (logistics).
- `/TransportExecutionPlan/cac:TransportContract/cac:ContractDocumentReference/cbc:ID` = `FRC-CON-2026-005-A1`: does not resolve to an example — refuted as a broken reference: a contract amendment the flow does not model, named unambiguously (logistics).
- `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: implausible size for a rail freight operator — refuted because nothing in the flow contradicts it (parties).
- `/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Valdara Industries`: bill-to party under the delivery terms — refuted: DAP, the seller pays the carriage, and 10 bills Valdara (parties).

## Changed in the merge
- logistics/F1 → F1 and F3: split into the service code and the From/To locations (different elements, different fixes); Needs decision yes changed to no, since the preferred option is an encoding change and only option (c)/(b) would change the flow.
- context/F3 → F3: Medium raised to High (broad, logistics): the hub as destination contradicts the plan's own instructions, delivery and contract description.
- broad/F8, context/F8, logistics/F4 → F5: Needs decision yes changed to no (parties); aligned with the earlier merges.
- money/F2 → F7: severity Medium kept (broad, context, money), Needs decision yes taken from money (broad and context had no): the fix depends on which penalty the agreement means.
- broad/F9, context/F7, parties/F2 → F8: preferred option "drop" (parties).
- broad/F14 → F13 and F16: split into contacts and the location name, each combined with the parties findings.
- broad/F13 → F18 and F20: split into the waiting-time charge (with money/F3) and PassengerQuantity (with context/F11, logistics/F9).
- broad/F5 (Medium), context/F9 (Low, yes), logistics/F5 (Low) → F14: Low, no: it is a consistency question between identifiers, not a misuse of an element; using one identifier changes no party or document.
- context/F6 (Medium), broad/F12, logistics/F8 (Low) → F17: Low: the element is used as defined (time after an event); the problem is that nothing in the plan describes such a notice.
- F11 (registration date): added by the merge for consistency with the earlier merges.
