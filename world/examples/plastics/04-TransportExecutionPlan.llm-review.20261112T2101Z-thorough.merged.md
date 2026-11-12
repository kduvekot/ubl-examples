# LLM review: 04-TransportExecutionPlan.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/04-TransportExecutionPlan.xml`, Git blob `dc8723ba3179d86f1689569b00ab4ceab21fea05` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/04#F1 · High · Origin of the service contradicts the loading place of the same plan
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:PostalZone` = `4170`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- XPath: `/TransportExecutionPlan/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`
- Why: `FromLocation` is "The location of origin of the transport service referenced in the Transport Execution Plan". It names the carrier and gives Fiumella's own business address (the same as `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:BuildingNumber` = `52`, postal zone 4170), while the only shipment stage of the same plan loads at Rinova's quay and the note says the barge leaves from the quay next to the recovery plant (Rinova: Via del Riciclo 31, postal zone 4140). For a single-stage, single-leg service the origin is thus stated as two different places in one document. The request has the same problem (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Fiumella Barges`). The name of a location is the place, not the company.
- Condition: `FromLocation` names and locates the place where the service begins and agrees with `LoadingPortLocation` and the note (and with 03 and 06).
- Options: (a) `FromLocation` = Rinova's quay in Ferrano, with an address or identifier (preferred: the stage already says the goods are loaded there); (b) if the barge does start at the carrier's base, describe that empty run as a separate stage and say so.
- Needs decision: no
- From: broad, logistics, parties, context

### plastics/04#F2 · High · Agreed payment term contradicted by the freight invoice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `07-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `07-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-22`
- Why: the plan agrees 30 days net from the consignment note. The consignment note is the waybill (`06-Waybill.xml:/Waybill/cbc:Name` = `Inland waterway consignment note under the CMNI`), issued `06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`, so payment is due 2026-05-19, net. The freight invoice for this transport counts 30 days from its own issue date (`07-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-22`, due 2026-05-22) and adds a 2 % settlement discount. Two documents of the same transport contract state different due dates and terms (verified in the merge).
- Condition: the payment term of the plan and the due date, discount and terms of `07-Invoice.xml` agree (same start of the period, same due date, a discount either agreed in the plan or absent from the invoice).
- Options: (a) bring the invoice in line with the plan (due 2026-05-19, no discount) (preferred by broad and the merge: the plan is the agreed contract the invoice executes); (b) word the plan's term as the carrier bills (30 days from invoice, 2 % within 10 days), since those are the carrier's standard terms (preferred by money).
- Needs decision: no
- From: broad, money

### plastics/04#F3 · Medium · Province of Urvanian addresses in Region
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity` ("such as the name of its county, province, or state"), as the Bayvarran address of the same plan does (`/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Coastal State`). No `languageID`. 219 occurrences in 104 of the 250 XML examples.
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; where given, it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) drop where the postal code identifies the place; (c) keep only if Ferrano is an economic region, recorded.
- Needs decision: no
- From: broad, parties, context

### plastics/04#F4 · Medium · Stationary-service location without a stationary service
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Fiumella Barges`
- Why: `AtLocation` is "The location of a transport service (e.g., terminal handling service) that does not require transport movement". The plan has no such service: the main service is the barge (`/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RIVERBARGE`) and the only additional one is the pre-arrival notice (`/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`), given to the consignee. The value is only the carrier's name, not a place (IND5/IND6).
- Condition: `AtLocation` is absent, or names the place of a service without movement that the plan contains.
- Options: (a) remove it (preferred: no such service exists in the story); (b) add the stationary service (e.g. storage or handling at a quay) with its place.
- Needs decision: no
- From: broad, context; logistics (Low); parties (grouped with F1)

### plastics/04#F5 · Medium · Late-payment percentage used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: `PaymentTerms/PenaltySurchargePercent` is "The penalty for payment after the settlement period, expressed as a percentage of the payment": a surcharge the debtor pays for paying late. Here it carries the carrier's penalty for delivering late (per day, capped at 25 %), owed by the carrier to the transport user: the opposite direction and another event. The parent `PenaltyPaymentTerms` ("Terms of payment applying to a penalty specified in the transport execution plan") can hold a delivery penalty, but not through this element; the per-day basis and the cap are only in the note. The skill names this case. The same note and percentage occur 3 times in the XML examples (context part, `grep -rh --include='*.xml' -B3 'PenaltySurchargePercent' world/examples`).
- Condition: no element defined for late payment carries the late-delivery penalty; the penalty is stated in text (or an element whose definition fits) and its rate, basis and cap agree with that text.
- Options: (a) keep the penalty in the note only and drop `PenaltySurchargePercent` (preferred); (b) if a late-payment surcharge is also agreed, state it separately with its own text.
- Needs decision: no
- From: broad, money, context

### plastics/04#F6 · Medium · The plan does not say what is carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: the Transport Execution Plan is "used in the negotiation of a transport service between a transport user and a transport service provider"; this one confirms capacity (`/TransportExecutionPlan/cbc:DocumentStatusReasonDescription` = `Capacity available on the requested day.`) for a consignment that has only an ID, a gross weight, a consignee and a stage: no description, packages or volume. The goods are 120 jumbo bags of PE granulate, 204 m³ gross (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`), which is what decides the barge space. Same gap as in the request (03 F3).
- Condition: the plan's consignment states what is carried (description, number and type of packages, ideally volume), consistent with 03 and 06.
- Options: (a) carry the same goods description and package count as the request once that is fixed (preferred: the plan confirms what was requested); (b) at least `TotalPackagesQuantity` and `GrossVolumeMeasure` on the consignment.
- Needs decision: no
- From: broad, logistics, context

### plastics/04#F7 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language, already in `Language/ID`. All 362 `LocaleCode` elements, in 213 of the 250 XML examples, carry this value.
- Condition: a locale such as `en-XB` from a locale list named in `listID`, or no `LocaleCode`.
- Options: (a) drop it (preferred); (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### plastics/04#F8 · Low · The request's "Please confirm by return." repeated in the confirmation
- XPath: `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`
- Why: `TransportUserRemarks` are "Remarks from the transport user regarding the transport operations referred to in the Transport Execution Plan". The remark asks for an answer to the request (03); it is not about the transport operations, and this plan is that answer (status `Confirmed`).
- Condition: the plan carries only transport-user remarks that concern the transport operations.
- Options: (a) leave the remark out of the plan (preferred).
- Needs decision: no
- From: context

### plastics/04#F9 · Low · Italian text tagged as English
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- Why: these `en-XU` renderings are Italian ("Banchina del Fiume", "River quay"; "Via del Riciclo", "Recycling street") and the legal form is Italian with an English gloss, while Bayvarran streets are English. 101 of the 250 XML examples show the pattern (parties part). Counter-argument (broad and context parts refuted the same candidate in `01-Order.xml`): Italianate exonyms are the world's convention for Urvanian names in English. The merge cannot settle it for street names; the legal form is a description, not a name, and is the stronger case.
- Condition: every rendering tagged `en-…` is English or a proper name used as such in English, and the convention is recorded in the world story if meant.
- Options: (a) record the convention and render the legal form in English (preferred); (b) translate all renderings; (c) drop the second rendering where the local form suffices.
- Needs decision: yes
- From: parties

### plastics/04#F10 · Low · All three companies registered on 1 January 1996
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Three companies in two registers share New Year's Day 1996; 271 occurrences in 181 of the 250 XML examples (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`). A default value (IND5) unless the story explains it.
- Condition: individual registration dates, or the shared date explained in the world's history, or the element absent.
- Options: (a) individual dates (preferred); (b) record a general (re-)registration in the story; (c) drop where no history is known.
- Needs decision: yes
- From: broad, parties, context

### plastics/04#F11 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Rinova receives the plan as transport user, so its contact is the shipping desk, not sales customer service. The consignee unloads the barge and is notified before arrival (`/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`), so its contact is goods receipt, not a sales order desk.
- Condition: contacts fit the transport roles (job title and department agree with the role), or are absent.
- Options: (a) role-specific contacts (preferred); (b) drop contacts the plan does not need.
- Needs decision: no
- From: broad, parties, context

### plastics/04#F12 · Low · Rinova's waste-recovery permit in a transport plan for a product
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: the permit (Basel Annex IV R3) plays no part in carrying a product (HS 390110 granulate), and in a transport document can suggest a waste shipment. It is in 14 XML examples, all 11 of this flow: master data copied into every document (section 4.8; IND5).
- Condition: the permit appears only in documents that act on it.
- Options: (a) remove it (preferred); (b) if the recycled-content claim is to rest on it, tie it to the item's certificate in documents that carry the item.
- Needs decision: no
- From: broad, parties, context

### plastics/04#F13 · Low · Signature identifier unrelated to the document
- XPath: `/TransportExecutionPlan/cac:Signature/cbc:ID` = `FB-SIG-882`
- Why: `Signature/ID` is "An identifier for this signature". The number 882 is that of the order (`01-Order.xml:/Order/cbc:ID` = `RP-PO-26-0882`), not of this plan (`/TransportExecutionPlan/cbc:ID` = `FB-TEP-26-0886`), and the signature carries nothing else (no date, method or attachment), so it is unclear what was signed and how. (The context part of `05-ExportCustomsDeclaration.xml` cites this ID as an example of a party's own numbering; the merge does not follow, since the number belongs to another party's document.)
- Condition: the signature's ID identifies a signature on this plan in the signatory's own numbering, and the signature says what is needed to rely on it, or it is absent.
- Options: (a) an ID derived from the plan, plus signing date or method (preferred); (b) remove the signature.
- Needs decision: no
- From: broad

### plastics/04#F14 · Low · Destination named after the consignee, with its business address
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`
- Why: `ToLocation`, "The destination location for the transport service", is the consignee's company name and business address (Estuary Road 28, Old town), while the plan unloads at the river quay, the CPT place of the order. Whether Estuary Road 28 is at that quay is not stated, so a contradiction cannot be shown (unlike F1); the name of a location is the place, not the company.
- Condition: the destination is the unloading place, named as a place, and agrees with `UnloadingPortLocation`.
- Options: (a) `ToLocation` = the river quay in Lumeport (preferred); (b) if Rivermouth has its own quay at Estuary Road 28, name it so in both `ToLocation` and the unloading port.
- Needs decision: no
- From: broad, parties; logistics and context (grouped with F1 there)

### plastics/04#F15 · Low · Brokerage commission to a broker who does not appear
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, paid by the barge operator to the barge broker that found the barge for this voyage.`
- Why: `CommissionPaymentTerms` is "Terms of payment applying to a commission specified in the transport execution plan". Rinova asked Fiumella's chartering desk directly (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Chartering desk`), under a framework agreement `RR-FB-FW-2026`, and no broker appears in any example of the flow; a commission paid by the operator to an unnamed third party is no term between the parties of this plan (IND5/IND6). Counter-argument (money part, which refuted it): brokerage clauses on freight are a standard part of charter terms, and `CommissionPaymentTerms` is defined for exactly that. The merge accepts that the element fits, but the note says a broker "found the barge for this voyage", which the direct booking in 03 contradicts; whether the story has a broker cannot be settled here.
- Condition: either the flow contains the broker that found the barge (identifiable, and the commission concerns the parties of the plan), or the plan carries no commission terms.
- Options: (a) remove the commission terms (preferred: the booking is direct under a framework agreement); (b) introduce the broker into the flow.
- Needs decision: yes
- From: broad, context (money refuted it)

### plastics/04#F16 · Low · Commission and penalty are percentages of a freight the plan never states
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, …`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: the confirmed plan is the transport contract; two of its terms are a percentage of "the freight", but the plan states no freight rate or amount. The rate appears only afterwards, in `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400` and `07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `1495` per tonne (120 t × 1 495 = 179 400, checked). `Consignment` in the plan can carry a `FreightAllowanceCharge`.
- Condition: the agreed freight (rate per tonne, or amount) is stated in the plan, or a document holding it is referenced, and equals what the waybill and the invoice use.
- Options: (a) add the freight to the plan's consignment as a freight charge (1 495 `XUF` per tonne, 179 400 `XUF` for 120 t) (preferred); (b) reference a price list or the framework contract that holds the rate.
- Needs decision: no
- From: money

### plastics/04#F17 · Low · Post-event delay on a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PreEventNotificationDurationMeasure` = `2`
- Why: the requirement is a pre-arrival notice two hours before arrival (as `/TransportExecutionPlan/cbc:TransportServiceProviderRemarks` = `Collection as requested; notice two hours before arrival.` says). `PostEventNotificationDurationMeasure` is "The length of time between the occurrence of a given event and the issuance of a notification"; a notice due before arrival has no post-event delay, and nothing in the plan says what is notified one hour after arrival.
- Condition: the pre-arrival requirement carries only the pre-event duration (2 h); a post-event notice, if wanted, is its own requirement with its own type.
- Options: (a) drop the post-event duration (preferred); (b) add a second requirement (arrival or delivery) for the one-hour post-event notice.
- Needs decision: no
- From: broad (Medium), logistics, context

### plastics/04#F18 · Low · Notification location is the notified company
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Rivermouth Packaging`
- Why: `NotificationLocation` is "A location at which a notification will be issued". The pre-arrival notice is issued from the barge and received by Rivermouth, which is already the `NotifyParty`; the value is a company name, not a place.
- Condition: the notification location is the place where the notice is issued, or the element is absent.
- Options: (a) remove it, since the notify party already says who receives it (preferred); (b) name the place from which it is issued.
- Needs decision: no
- From: broad, logistics, parties, context

### plastics/04#F19 · Low · Waiting-time charge without currency, implausibly low
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:ServiceChargePaymentTerms/cbc:Note` = `Waiting time 40 per hour beyond two hours.`
- Why: the rate has no currency. Read in the contract's currency `XUF`, 40 `XUF` an hour is negligible next to a freight of 1 495 `XUF` per tonne, 179 400 `XUF` for this voyage (about 0.02 % of the freight per hour), or 0.40 `XBL` at the rate of 100 `XUF` = 1 `XBL` used throughout the examples; with recycled PE granulate at roughly 1 000 EUR per tonne as a scale (83 200 `XUF` per tonne here), 40 `XUF` is about half a euro an hour, far below any real waiting or demurrage charge for a crewed barge (own knowledge).
- Condition: the waiting-time rate states its currency and has a plausible size against the freight.
- Options: (a) state the currency and a plausible hourly amount (preferred); (b) express it as a share of the freight.
- Needs decision: no
- From: broad, money

### plastics/04#F20 · Low · Consignee's bank account in the transport plan
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". The consignee pays nothing under the plan (`/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`); the account is copied master data (section 4.8). It appears in 14 XML examples.
- Condition: the consignee party carries no financial account unless the plan uses it.
- Options: (a) drop it (preferred); (b) keep it only with a freight-collect arrangement involving the consignee.
- Needs decision: no
- From: broad, money, parties, context

### plastics/04#F21 · Low · Voyage number in the element for a regular service schedule
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`
- Why: `JourneyID` is "An identifier for the regular service schedule of this means of transport". Nothing in the flow says Fiumella runs a regular service; the value reads as the number of a voyage booked for this consignment. Counter-argument (logistics part, which refuted it): a voyage number of a barge in a regular river service is the common reading of this element, and the waybill's carrier-assigned ID builds on it (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `FB4-26-031/2`, a part load, which suggests a sailing shared with other cargo). Whether the voyage belongs to a regular service is a story question the merge cannot settle.
- Condition: `JourneyID` identifies a regular service of which this is a sailing (and the story says so), or the voyage number is carried in an element whose definition fits it.
- Options: (a) keep `JourneyID` and make the regular downstream service visible in the story (preferred if true); (b) otherwise carry the voyage number as a carrier-assigned identifier of the stage or consignment.
- Needs decision: yes
- From: broad (logistics refuted it)

### plastics/04#F22 · Low · Exportation event without a place
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`
- Why: the exportation event (the goods leaving Urvania) has a date and time but no location; the place, the customs post at the river border, appears only in `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`. An exportation event is meaningless without where it happens.
- Condition: the exportation event has its location, consistent with the exit office of 05.
- Options: (a) add the border location to the exportation event (preferred).
- Needs decision: no
- From: broad

## Checked and consistent
- `/TransportExecutionPlan/cac:TransportExecutionPlanRequestDocumentReference/cbc:ID` = `RR-TR-26-0884` resolves to `03-TransportExecutionPlanRequest.xml`; parties, contract `RR-FB-FW-2026`, service window, consignment ID and gross weight agree; the plan is issued on the response deadline 2026-04-15.
- Event order (checked in the merge): takeover 2026-04-19 09:00, loading 13:30, exportation 2026-04-20 16:00, discharge 2026-04-22 08:00; all after the issue (2026-04-15 13:10), inside the service window and the validity period ending 2026-04-22. Loading to discharge is 2 d 18.5 h, takeover to discharge 2 d 23 h, consistent with `EstimatedTransitPeriod` 3 DAY. The same events, vessel, journey and master are in `06-Waybill.xml`.
- Direction downstream fits a voyage from Ferrano to the river mouth at Lumeport.
- Vessel: freight barge (Rec. 28 code 815), inland waterway mode 8, 1 210 GT / 860 NT; 120.48 t and about 204 m³ of cargo are a small part of what a dry barge of that size carries (about 1 500–2 500 t, own knowledge), consistent with a part load. Call sign `QUBF4` (the Q block is not allocated to any country by the ITU) and MMSI `297801042` (MID 297 not allocated, own knowledge) cannot be mistaken for real ones.
- `BillToParty` ("The Party who executes the Payment for the transport service") = Rinova, who bears the freight under CPT and receives `07-Invoice.xml`. No waiting time or late-delivery penalty is billed in 07, which agrees with delivery in the estimated 3 days.
- `DocumentStatusCode` `Confirmed` with reason `ASREQUESTED` agrees with the provider's remark "Collection as requested". Waiting-time terms in the provider's special terms and the service-charge terms agree (beyond two hours).
- Parties: sender, provider and signatory Fiumella; receiver, transport user and bill-to Rinova; consignee and notify party Rivermouth, as in 03; the skipper (Tomaso Riverra) is the same in 06. `check_ids.py`: the IBAN-like account passes.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate`: a user response deadline on a confirmed plan — refuted: in the UBL transport process the transport user still accepts or rejects the plan the provider returns. (from broad, context)
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TakeoverTransportEvent/cbc:OccurrenceTime` = `09:00:00`: takeover four and a half hours before loading (13:30) — refuted: taking over goods on the quay in the morning and loading in the afternoon is normal (CMNI). (from broad, logistics)
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`: an indicator without reason — refuted: the discharge lies in the future of the plan, so "not completed" is true. (from logistics, context; see also "Refuted in the merge")
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent`: an exportation event in main carriage — refuted: the barge leaves Urvania during main carriage. (from context)
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport` for a river barge — refuted: the aggregate is defined as "A vessel used for transport by water (not only by sea)". (from context)
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`: misuse of a regular-service identifier — refuted by logistics as the common reading of the element. The merge cannot settle it; kept as F21 with "Needs decision: yes". (from logistics)
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note`: a commission between the carrier and a broker who is not a party — refuted by money because brokerage clauses are standard and the element is defined for them. The merge disagrees in part; kept as F15. (from money)
- `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` could clash with a real ICD — refuted: not assigned in the real register (own knowledge). (from parties)
- `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped identifier (`BLUMXBLX`) could be a real BIC — refuted: positions 5–6 carry the user-assigned code `XB`. (from parties)
- `/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name`: the seller as bill-to party — refuted: under CPT the seller pays the carriage, and 07 bills Rinova. (from parties)

## Refuted in the merge
### broad/F14 (part) · Low · Completion indicator on one event only
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`
- Why (broad): all events of the plan lie in the future of its issue date (2026-04-15), but only the discharge says it is not completed, so the indicator adds nothing and implies something about the others by absence (IND6). Condition (broad): `CompletionIndicator` is absent or used consistently where it informs.
- Refuted because: the value is true (the plan precedes the voyage), and the absence of the indicator on the other events states nothing about them: no reader infers "completed" for a planned event in a plan issued days before it. The part of broad/F14 on the missing exportation location is kept as F22. Logistics and context refuted the same candidate.

## Changed in the merge
- broad/F1, logistics/F1, parties/F1, context/F1 → F1 (FromLocation, High) and F14 (ToLocation, Low): split, because only FromLocation contradicts another value of the same plan (the loading port and the note); the unloading port and the consignee's address cannot be shown to be different places. Parties' `AtLocation` part moved to F4.
- broad/F2, money/F1 → F2: combined; both options kept, preference of broad (invoice follows the plan).
- broad/F7, parties/F2, context/F5 → F3: combined.
- broad/F5, logistics/F3 (Low), context/F2, parties/F1 (part) → F4: combined at Medium (the element carries no place of a service its definition requires).
- broad/F3, money/F2, context/F3 → F5: combined.
- broad/F6, logistics/F2, context/F4 → F6: combined.
- broad/F8, parties/F3, context/F6 → F7: combined; preferred option "drop".
- parties/F8 → F9: counter-argument from the refutations in `01-Order.xml` added; preferred option changed.
- broad/F18, parties/F7, context/F13 → F10: combined; "Needs decision" yes.
- broad/F15, parties/F4, context/F12 → F11: combined.
- broad/F16 (part), parties/F6, context/F11 → F12: combined; "Needs decision" no instead of yes (parties).
- broad/F17 → F13: wording; note on the context part of 05 added.
- broad/F9, context/F7 → F15: combined; money's refutation added as counter-argument.
- broad/F4 (Medium), logistics/F4 (part), context/F8 (part) → F17: lowered to Low, because the post-event duration is a valid value of its element; the problem is that nothing in the plan says what it notifies, not a meaning other than the definition.
- broad/F12, logistics/F4 (part), parties/F9 (part), context/F8 (part) → F18: split out of the grouped findings, as its own element and condition.
- broad/F11, money/F4 → F19: combined.
- broad/F16 (part), money/F5, parties/F5, context/F10 → F20: combined; broad's grouping of the account with the permit split into F12 and F20.
- broad/F13 → F21: "Needs decision" changed from no to yes, with logistics' refutation as counter-argument.
- broad/F14 → F22: reduced to the missing location; the completion-indicator part refuted (see "Refuted in the merge").
