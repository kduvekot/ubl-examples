# LLM review: 04-TransportExecutionPlan.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### plastics/04#F1 · High · From and to locations contradict the loading and unloading places of the same plan
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`
- XPath: `/TransportExecutionPlan/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`
- Why: `FromLocation` is "the location of origin of the transport service" and `ToLocation` "the destination location". The plan names them after the carrier and the consignee and gives their postal business addresses (the carrier's own address, `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:BuildingNumber` = `52`, and the consignee's office in Estuary Road). The only stage of the same plan loads at Rinova's quay and unloads at the river quay of Lumeport, and the note says the barge starts at the quay next to the recovery plant. Origin and loading place, destination and unloading place, are therefore different places in one document for a single-stage, single-leg service. The same pair is in the request (03).
- Condition: `FromLocation` and `ToLocation` name and locate the places where the service starts and ends, and agree with `LoadingPortLocation` and `UnloadingPortLocation` (and the note), in 03, 04 and 06.
- Options: (a) preferred: make `FromLocation` Rinova's quay in Ferrano and `ToLocation` the river quay in Lumeport, with an address or identifier each, because the stage already says that is where the goods are loaded and unloaded; (b) if the barge does start at the carrier's base, describe that empty run as a separate stage and say so.
- Needs decision: no

### plastics/04#F2 · Medium · The plan's consignment does not say what is carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: The plan is used "in the negotiation of a transport service"; its consignment has an ID, a gross weight, a consignee and a stage, but no goods item, description, package count or volume. The carrier confirms capacity ("Capacity available on the requested day") for a cargo it is never told the size or kind of; 120 jumbo bags of about 1.7 m³ each (204 m³ in 06) is what decides the barge space. Same gap as in the request (03#F1).
- Condition: The plan's consignment describes the goods carried (description, number and type of packages, ideally volume), consistent with 03 and 06.
- Options: (a) preferred: carry the same goods description and package count as the request (once 03#F1 is fixed), because the plan confirms what was requested; (b) at least `TotalPackagesQuantity` and `GrossVolumeMeasure` on the consignment.
- Needs decision: no

### plastics/04#F3 · Low · AtLocation names a service location for which there is no service
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Fiumella Barges`
- Why: `AtLocation` is "the location of a transport service (e.g., terminal handling service) that does not require transport movement". The plan has no such service: the main service is the barge voyage and the additional service is a pre-arrival notice (`/TransportExecutionPlan/cac:AdditionalTransportationService/cbc:TransportServiceCode` = `NOTIFY`), which is given to the consignee, not performed at the carrier. The location has only the carrier's name.
- Condition: `AtLocation` is present only for a stationary service the plan actually contains, and then names that place.
- Options: (a) preferred: remove it, because no service of that kind exists in the story; (b) add a stationary service (e.g. storage or handling at a quay) if the story has one.
- Needs decision: no

### plastics/04#F4 · Low · Pre-arrival notification carries a post-event duration and a company as its location
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Rivermouth Packaging`
- Why: The requirement is a pre-arrival notice "two hours before arrival" (`PreEventNotificationDurationMeasure` = 2 HUR, matching the remarks). `PostEventNotificationDurationMeasure` is "the length of time between the occurrence of a given event and the issuance of a notification"; a notice that is due before arrival has no post-event delay, and nothing says what is notified one hour after arrival. `NotificationLocation` is "a location at which a notification will be issued"; the notice is issued from the barge, and the value is the notified company's name, which is already in `NotifyParty`.
- Condition: The requirement carries only the pre-event duration, unless a second, post-arrival notification exists (then as its own `NotificationRequirement` with its own type); `NotificationLocation` is absent or names a place where the notice is issued.
- Options: (a) preferred: drop the post-event duration and the notification location; (b) add a separate arrival notification with the one-hour delay if the story wants one.
- Needs decision: no

## Checked and consistent
- Event order of the planned stage: takeover 2026-04-19 09:00, loading 13:30, exportation 2026-04-20 16:00, discharge 2026-04-22 08:00; all after the plan's issue (2026-04-15 13:10), all inside the service window 2026-04-19 to 2026-04-22 and the validity period ending 2026-04-22. Loading to discharge is 2 d 18.5 h, takeover to discharge 2 d 23 h, consistent with `EstimatedTransitPeriod` = 3 DAY.
- Direction `DS` (downstream) fits the note ("down the river") and the destination at the river mouth (Estuary Road, Rivermouth).
- Vessel: freight barge (Rec. 28 code 815), inland waterway mode 8, dry cargo barge of GT 1210 / NT 860; 120.48 t and about 204 m³ of cargo (06) are a small part of what a barge of that size carries (a dry-cargo barge of about 1200 GT carries in the order of 1500–2500 t, own knowledge), consistent with a part load (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `FB4-26-031/2`).
- Call sign `QUBF4`: the Q block is not allocated to any country by the ITU, so it cannot be mistaken for a real call sign. MMSI `297801042`: MID 297 is not in the ITU's allocated MIDs as far as I know (own knowledge).
- Vessel, journey, master and events are identical in 06.
- The request reference `RR-TR-26-0884` resolves to 03; the contract `RR-FB-FW-2026` is the same as in 03.

## Considered and refuted
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `FB4-26-031`: suspected misuse, because the definition speaks of "the regular service schedule" and this looks like a single voyage — refuted because a voyage number of a barge in a regular river service is the common reading of this element, and the consignment's carrier-assigned ID (06) builds on it.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TakeoverTransportEvent/cbc:OccurrenceTime` = `09:00:00`: suspected a contradiction with the loading at 13:30 — refuted because the carrier taking over the goods on the quay in the morning and loading them in the afternoon is a normal sequence.
- `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false`: suspected an indicator without reason — refuted because the plan is issued before the voyage, so "not completed" is true.
