# LLM review: 04-TransportExecutionPlan.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/04-TransportExecutionPlan.xml`, Git blob `dc8723ba3179d86f1689569b00ab4ceab21fea05` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/04#F1 · High · Origin of the service contradicts the loading place
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- Why: FromLocation is "The location of origin of the transport service". It is the carrier's own office address (same as `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`, postal zone 4170), while the same plan loads the goods at Rinova's quay and the note says the barge leaves "from the quay next to the recovery plant" (Rinova: Via del Riciclo 31, postal zone 4140). The name is a company name, not a place. The request has the same problem (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Fiumella Barges`).
- Condition: FromLocation is the place where the service begins (the loading quay), named as a place, and agrees with `LoadingPortLocation` and the note.
- Options: (a) FromLocation = Rinova's quay in Ferrano (preferred); (b) if the barge's voyage starts at its base, make that explicit and keep it apart from the place of takeover.
- Needs decision: no

### plastics/04#F2 · High · Agreed payment terms contradicted by the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- Why: The plan agrees 30 days net from the consignment note. The consignment note is dated 2026-04-19 (`06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`), so payment is due 2026-05-19 with no discount. The freight invoice instead offers a 2 % settlement discount and is due 30 days from its own date (`07-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`, `07-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-22`).
- Condition: the payment terms of the plan and of the freight invoice (`07-Invoice.xml`) agree in start date, period and discount.
- Options: (a) bring the invoice in line with the plan (preferred: the plan is the contract basis); (b) change the plan's terms to what the carrier invoices.
- Needs decision: no

### plastics/04#F3 · Medium · Late-payment percentage used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: PenaltySurchargePercent is "The penalty for payment after the settlement period, expressed as a percentage of the payment". The note describes a penalty for late delivery (per day late, as a share of the freight), which is a different thing; the element states a late-payment surcharge the parties did not agree. The skill names this case ("a late-payment surcharge used for late delivery").
- Condition: `PenaltySurchargePercent` is either absent or a late-payment surcharge; a late-delivery penalty is expressed in text (or another element whose definition fits).
- Options: (a) keep the late-delivery penalty in the note only and drop `PenaltySurchargePercent` (preferred); (b) if a late-payment surcharge is also agreed, state it separately.
- Needs decision: no

### plastics/04#F4 · Medium · Post-event delay on a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: The notification is a pre-arrival notice (`NotificationTypeCode` `PREARRIVAL`, two hours before arrival, as `/TransportExecutionPlan/cbc:TransportServiceProviderRemarks` and the additional service `NOTIFY` say). PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given event and the issuance of a notification": a notice issued one hour after the arrival is not a pre-arrival notice. Both durations together contradict each other for one notification.
- Condition: the pre-arrival notification carries only the pre-event duration (2 h); any post-event notice (e.g. arrival confirmation) is a separate requirement with its own type.
- Options: (a) drop the post-event duration (preferred); (b) add a second notification requirement (arrival or delivery) for the one-hour post-event notice.
- Needs decision: no

### plastics/04#F5 · Medium · Stationary-service location without a stationary service
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Fiumella Barges`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does not require transport movement". The plan has no such service: the main service is river carriage and the additional service is a pre-arrival notice. The location is only a company name. It carries no information the plan uses (IND5/IND6).
- Condition: `AtLocation` is present only for a service without movement that the plan contains, and then names that place.
- Options: (a) remove it (preferred); (b) add the stationary service (e.g. a terminal handling or storage) the story needs, with its location.
- Needs decision: no

### plastics/04#F6 · Medium · The plan does not say what is carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: The plan is the document in which the transport service is agreed; its consignment gives only a gross weight, with no description, packages or volume (as in the request, `03-TransportExecutionPlanRequest.xml`). The goods are 120 jumbo bags of PE granulate, 204 m³ gross (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`), which a barge operator plans the hold for.
- Condition: the agreed plan states what is carried: description, number and type of packages, gross weight and volume.
- Options: (a) add a goods item or package description to the consignment (preferred); (b) at least a goods description.
- Needs decision: no

### plastics/04#F7 · Medium · Province of Urvanian addresses in Region
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as in the Bayvarran address of the same plan (`/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Coastal State`). No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/04#F8 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is a language, already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/04#F9 · Low · Brokerage commission to a broker who does not appear
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, paid by the barge operator to the barge broker that found the barge for this voyage.`
- Why: CommissionPaymentTerms is "Terms of payment applying to a commission specified in the transport execution plan". The transport user booked the barge directly with the operator (`03-TransportExecutionPlanRequest.xml` is sent from Rinova to Fiumella, under a framework agreement `RR-FB-FW-2026`); no broker is a party in any example of the flow. A commission paid by the operator to an unnamed third party is not a term between the two parties of this plan, so it has no visible business reason here (IND5/IND6).
- Condition: either the commission terms are absent, or the broker exists in the story (and is identifiable) and the commission concerns the parties of the plan.
- Options: (a) remove the commission terms (preferred: the booking is direct under a framework agreement); (b) introduce the broker into the flow.
- Needs decision: yes

### plastics/04#F10 · Low · Destination named after the consignee, with its business address
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`
- Why: ToLocation, "The destination location for the transport service", is the company's business address (Estuary Road 28, Old town), while the plan unloads at the river quay, the CPT place of the order. The location's name is a company, not a place; whether the address is at the quay is not stated.
- Condition: the destination is the unloading place, named as a place, and agrees with `UnloadingPortLocation`.
- Options: (a) ToLocation = the river quay in Lumeport (preferred); (b) name the quay and keep the address if the quay is at Estuary Road 28.
- Needs decision: no

### plastics/04#F11 · Low · Waiting-time charge without currency and implausibly small
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- Why: The rate has no currency. Read as Ferra, 40 XUF per hour is negligible next to a freight of 1 495 XUF per tonne, 179 400 XUF for this voyage (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`); a barge with crew waiting costs far more than 0.02 % of the freight per hour (own judgement).
- Condition: the waiting-time rate states its currency and has a plausible size against the freight.
- Options: (a) give a currency and a rate in proportion (preferred); (b) state it as a percentage of the freight.
- Needs decision: no

### plastics/04#F12 · Low · Notification location is the consignee
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Rivermouth Packaging`
- Why: NotificationLocation is "A location at which a notification will be issued". The pre-arrival notice is issued by the barge on its way and received by Rivermouth (the notify party); the consignee is where it arrives, not where it is issued. The value is a company name.
- Condition: the notification location is the place where the notice is issued (or the element is absent).
- Options: (a) remove it, as the notify party already says who receives it (preferred); (b) name the place from which it is issued.
- Needs decision: no

### plastics/04#F13 · Low · Voyage number in the element for a regular service schedule
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`
- Why: JourneyID is "An identifier for the regular service schedule of this means of transport". This is a one-off voyage of the barge `Fiumella IV` booked for this consignment, not a scheduled service; the value reads as a voyage number.
- Condition: `JourneyID` identifies a regular service, or the voyage number is carried in an element whose definition fits it.
- Options: (a) keep `JourneyID` if Fiumella runs a regular downstream service of which this is a sailing, and say so (preferred if true); (b) otherwise move the voyage number to the shipment stage or consignment as carrier-assigned identifier.
- Needs decision: no

### plastics/04#F14 · Low · Exportation event without a place, completion indicator on one event only
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`
- Why: The export event (leaving Urvania) has a date and time but no location; the place, the customs post at the river border, is only in `05-ExportCustomsDeclaration.xml`. All events of the plan lie in the future of its issue date (2026-04-15), but only the discharge says it is not completed, so the indicator adds nothing and implies something about the others by absence (IND6).
- Condition: the export event has its location; `CompletionIndicator` is absent or used consistently where it informs.
- Options: (a) add the border location to the exportation event and drop the indicator (preferred); (b) leave both as they are only if the world treats the indicator as meaningful for discharge.
- Needs decision: no

### plastics/04#F15 · Low · Contacts do not fit the roles
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- Why: The transport user's contact is a sales customer-service officer, not the shipping desk that agrees the plan; the consignee's contact, notified before arrival and unloading the barge (`/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`), is a sales order desk, not goods receipt.
- Condition: contacts fit the transport roles.
- Options: role-specific contacts (preferred) or neutral general contacts.
- Needs decision: no

### plastics/04#F16 · Low · Copied master data: consignee's bank account and the waste permit
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The consignee pays nothing under the plan (bill-to is Rinova), and the waste-recovery permit plays no part in carrying a product (HS 390110 granulate); both are master data the plan does nothing with (section 4.8).
- Condition: neither appears in the plan.
- Options: remove both (preferred).
- Needs decision: no

### plastics/04#F17 · Low · Signature identifier unrelated to the document
- XPath: `/TransportExecutionPlan/cac:Signature/cbc:ID` = `FB-SIG-882`
- Why: The number 882 matches the order (`RP-PO-26-0882`), not this plan (`FB-TEP-26-0886`), and the signature carries nothing else (no date, method or attachment), so it is unclear what was signed and how.
- Condition: the signature's ID identifies a signature on this plan, and the signature says what is needed to rely on it (or it is absent).
- Options: (a) an ID derived from the plan, plus signing date or method (preferred); (b) remove the signature.
- Needs decision: no

### plastics/04#F18 · Low · All three parties registered on 1 January 1996
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for three companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

## Checked and consistent
- `/TransportExecutionPlan/cac:TransportExecutionPlanRequestDocumentReference/cbc:ID` = `RR-TR-26-0884` resolves to `03-TransportExecutionPlanRequest.xml`; parties, contract `RR-FB-FW-2026`, service window, consignment ID and gross weight agree; the plan is issued on the response deadline 2026-04-15.
- Event order: takeover 2026-04-19 09:00, loading 13:30, exportation 2026-04-20 16:00, discharge 2026-04-22 08:00; loading to discharge is 2 d 18.5 h, consistent with the estimated transit of 3 days and with the service end 2026-04-22. The same events and vessel data are in `06-Waybill.xml`.
- Vessel: radio call sign `QUBF4` (the Q prefix is not allocated to any country by the ITU) and MMSI `297801042` (MID 297 is not allocated, own knowledge) cannot be mistaken for real ones. A dry barge of 1 210 GT carries 120 t / 204 m³ easily.
- Direction downstream fits a voyage from Ferrano (Urvania) to the river mouth at Lumeport.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate`: a user response deadline on a confirmed plan — refuted: in the UBL transport process the transport user still accepts the plan the provider sends, so a deadline for that is meaningful.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TakeoverTransportEvent/cbc:OccurrenceTime`: takeover (09:00) four and a half hours before loading (13:30) — refuted: takeover at the quay before loading is normal under the CMNI.
