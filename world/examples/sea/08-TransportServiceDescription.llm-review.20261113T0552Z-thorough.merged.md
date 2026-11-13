# LLM review: 08-TransportServiceDescription.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/08-TransportServiceDescription.xml`, Git blob `3b64d9a508af69f9f2be5711a0061f17a39e8741` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 37375cd 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/08#F1 · High · Booking deadline already past when the service is offered, and the booking comes after it
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationDate` = `2026-05-09`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationTime` = `10:00:00`
- XPath: `/TransportServiceDescription/cbc:IssueDate` = `2026-05-09`
- XPath: `/TransportServiceDescription/cbc:IssueTime` = `12:03:00`
- Why: `NominationDate`/`NominationTime` are "In a transport contract, the deadline date by which this transportation service has to be booked" and its time. The description offering the service (`ResponseCode` `OFFERED`) is issued 2 h 03 min after that deadline, so the booking window is closed when it is offered. The booking itself is the forwarder's instruction to the carrier the next morning (`12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:IssueDate` = `2026-05-10`, 09:15), after the deadline, and the carrier accepts it (booking `TWL-BK-26-55710` on the bill of lading).
- Condition: the nomination deadline lies after the issue of the description, no earlier than the booking in `12-ForwardingInstructions.xml`, and before the sailing it is for.
- Options: (a) preferred: a deadline between the booking (2026-05-10 09:15) and the sailing, e.g. 2026-05-12 (a usual cut-off two days before sailing); (b) drop the nomination deadline from a general service description.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### sea/08#F2 · High · Weekly sailing day Friday, but the flow's sailing is on Thursday 2026-05-14
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: `WeekDayCode` `5` is Friday (UBL WeekDayCode list); 2026-05-14 is a Thursday (recalculated with Python `datetime`). The vessel actually leaves Lumeport on Thursday 2026-05-14 at 18:10 (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`), so the scheduled weekday contradicts the actual sailing of the same service in another example. The context part read the untyped event as the cargo cut-off of a Friday sailing, supported by the manifest's estimated departure on Friday 15 May (`15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`); that reading saves 08's own two values but not the contradiction with 13's actual Thursday departure. (Whether 13 and 15 agree with each other belongs to their reviews.)
- Condition: the scheduled weekday, the dated event of the service and the actual sailing of the flow agree.
- Options: (a) preferred: `WeekDayCode` `4` (Thursday), matching the event and the actual departure (and the manifest's estimate then on 14 May); (b) move the sailing to Friday, which changes the dates of the bill of lading, status and manifest.
- Needs decision: no
- From: broad (F2), logistics (F2); context (inside F2, Medium, with the cut-off reading)

### sea/08#F3 · High · "Two days at sea" between ports the flow places 3.2 nautical miles apart
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:TransportationServiceDescription` = `A weekly feeder sailing from Lumeport to Selanu, two days at sea.`
- Why: the service takes two days from Lumeport to Selanu. The flow gives both ports coordinates on the same latitude 40°1.20′ S: Lumeport's container quay at 15°12.60′ W (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`) and the port of Selanu at 15°8.40′ W (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`). Recalculated: 4.2′ × cos 40° = 4.2 × 0.766 = 3.2 nautical miles; a feeder at 12–15 knots covers that in about 15 minutes. The common transportation report places the ship "120 nautical miles west of Selanu" during the passage (`16-CommonTransportationReport.xml`). The duration, the distances and the coordinates of the same two ports cannot all be true. High because examples describing the same objects contradict each other; needs decision because which value is right depends on the world's map scale (as sea merger c decided for 16).
- Condition: the passage duration, the distances stated in the flow and the coordinates of the two ports are consistent with each other.
- Options: (a) preferred if the map scale allows: keep two days and correct the port coordinates to positions several hundred nautical miles apart (the duration recurs in the manifest and the report); (b) keep the coordinates and shorten the passage, which changes the voyage in several documents.
- Needs decision: yes (map scale)
- From: logistics (F3)

### sea/08#F4 · Medium · LocaleCode holds a language code (two places)
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; both hold the ISO 639 language code of `Language/ID`. 362 such elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: each `LocaleCode` is absent or a locale from a locale list.
- Options: (a) preferred: drop them; (b) `en-XB` from a list of language tags.
- Needs decision: no
- From: broad (F5), parties (F1), context (F5)

### sea/08#F5 · Medium · A gate in AdditionalStreetName of the receiver's postal address
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`). Under CIF the container is stuffed at Marrowdale and trucked to Lumeport, so where the carrier's haulier needs the gate, a pickup location carries it.
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address (and give it in a pickup location where one is arranged).
- Needs decision: no
- From: broad (F6), parties (F2), context (F9, Low)

### sea/08#F6 · Medium · A kind of service in the element for the extent of the service
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: as in 07#F3: `TransportServiceCode` is "A code signifying the extent of this transportation service (e.g., door-to-door, port-to-port)"; "Container liner service" is a kind of service. The described sailing Lumeport–Selanu is port-to-port.
- Condition: an extent code (e.g. port-to-port); the container liner character given elsewhere (`Name`, description, transport mode).
- Options: (a) preferred: port-to-port; (b) redefine the world list as extents.
- Needs decision: no
- From: context (F4)

### sea/08#F7 · Medium · The service classified with a goods code for seats
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:CommodityClassification/cbc:ItemClassificationCode` = `38111`
- Why: under `TransportationService`, `CommodityClassification` is "A classification of this transportation service". CPC 38111 "Seats, primarily with metal frames" classifies Lumeway's benches, not a liner service; the goods the service takes are stated in `SupportedCommodityClassification` (`GEN`) and `TariffClassCode` `FAK`. A service would be classified by a CPC service class for freight transport by water (own knowledge), or not at all.
- Condition: the service's `CommodityClassification` classifies the service, or is absent.
- Options: (a) preferred: drop it; (b) a CPC code for coastal or transoceanic freight transport services.
- Needs decision: no
- From: broad (F4), context (F3)

### sea/08#F8 · Medium · Transport event without type or location
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:CompletionIndicator` = `false`
- Why: `TransportEvent` is "One or more transport events taking place in this transportation service". It has a date, a time and "not completed", but no `TransportEventTypeCode`, description or `Location`, so a receiver cannot tell whether 18:00 on 14 May is the departure, the cargo cut-off or an arrival (the checklist: an event needs a location or type where it would otherwise be meaningless). The flow's actual departure at 18:10 suggests the departure; context suggests a cut-off (F2).
- Condition: the event says what it is (type code or description) and where it takes place, consistent with F2.
- Options: (a) preferred: type "departure" with location `XBLMP`; (b) the cargo cut-off at the Lumeport terminal, typed as such; (c) the sailing as an estimated departure in the service's shipment stage.
- Needs decision: no
- From: broad (F3), logistics (F4), context (F2)

### sea/08#F9 · Low · Signature with only an ID and a signatory
- XPath: `/TransportServiceDescription/cac:Signature/cbc:ID` = `TWL-SIG-TSD`
- XPath: `/TransportServiceDescription/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Tidewell Ocean Lines`
- Why: the signature has no method, attachment or validation; nothing is signed. 137 of the 147 `Signature` aggregates of the world hold only `ID` and `SignatoryParty` (lxml count over `world/examples/*/*.xml`); earlier merges kept this as Low/yes (see 01#F6, 07#F5). No part raised it; added in the merge for consistency within the flow. (Broad's refuted prefix question is under Considered and refuted.)
- Condition: either the signature carries what makes it one, or the document has no `Signature`; one rule across the world.
- Options: (a) preferred: drop it; (b) document the convention.
- Needs decision: yes (world-wide convention)
- From: merge (no part)

### sea/08#F10 · Low · Legal and tax master data of both parties in a service description
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: the description has no legal, tax or customs effect; share capital, tax numbers, registrations and Lumeway's customs-trader number play no role in it (section 4.8).
- Condition: sender and receiver carry identification, name, contact and endpoint only, or the document has a reason for the rest.
- Options: (a) preferred: reduce both parties.
- Needs decision: no
- From: context (F8); the customs-trader number added in the merge

### sea/08#F11 · Low · Lumeway's sales customer service as receiver of a carrier's offer
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway receives the offer as a transport user choosing a sailing; its contact should be the function that books transport, not the sales customer service that serves its buyers (same contact as in 07, 07#F7).
- Condition: the receiver's contact is the function that books transport, or absent.
- Options: (a) preferred: a shipping/logistics contact of Lumeway; (b) no contact.
- Needs decision: no
- From: broad (F8), parties (F3), context (F7)

### sea/08#F12 · Low · Shipment stage of the service without ports; route only in text
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ShipmentStage/cbc:TransportModeCode` = `1`
- Why: the service's single stage gives only the mode; the route Lumeport–Selanu is only in `Name` and `TransportationServiceDescription`, although both ports are identified in the flow by LOCODE (`XBLMP`, `XLSEL`, e.g. `06-OrderResponse.xml:/OrderResponse/cac:DeliveryTerms/cac:DeliveryLocation/cbc:ID` = `XLSEL`).
- Condition: the stage carries its loading and unloading ports.
- Options: (a) preferred: `LoadingPortLocation` `XBLMP` and `UnloadingPortLocation` `XLSEL`.
- Needs decision: no
- From: logistics (F5)

### sea/08#F13 · Low · Emission of the service without what it applies to
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EnvironmentalEmission/cbc:ValueMeasure` = `380`
- Why: "An environmental emission resulting from this transportation service" of 380 kg CO2e, with no base (per container, per TEU, per sailing) and no method. For a whole two-day sailing of a 1,000 TEU feeder it is far too low (own knowledge: some 15–30 t of fuel a day at about 3.1–3.2 t CO2 per t of fuel, i.e. roughly 100–200 t CO2 per sailing); per 40-foot box it is plausible: logistics' figure of 380 / (7.9 t × about 1,150 km) ≈ 42 g CO2e per tonne-km, at the high end for a feeder (own knowledge 15–40 g). Note that 1,150 km rests on two days at about 13 knots, which F3 questions.
- Condition: the emission states what it refers to (e.g. `ValueFactorNumeric` with `ValueBaseMeasure` per container, and the method), and the value fits that base.
- Options: (a) preferred: base "1 container 40 ft" (or per TEU) with the calculation method; (b) drop it.
- Needs decision: no
- From: broad (F7), logistics (F6), context (F6)

## Checked and consistent
- The request reference `LD-DOC-26-0129` resolves to `07-TransportServiceDescriptionRequest.xml` (sender and receiver swapped, as expected); sender, signatory, transport service provider and responsible provider are all Tidewell Ocean Lines (`20411918`).
- Equipment: the offered `42G1` is among the supported types and is the container of the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:SizeTypeCode` = `42G1`); `45R1` unsupported and general cargo supported / bulk unsupported fit a dry container feeder; `TransportEquipment` (proposed) and `SupportedTransportEquipment` both with 42G1 are different statements (context).
- Capacity 1,000 TEU (unit `20`, twenty-foot container) for an island feeder; the vessel on the bill of lading has 9,940 GT, consistent with real feeders of about 1,000 TEU (own knowledge).
- Two days in `EstimatedDurationPeriod` agrees with the description text; validity 2026-05-09 to 2026-08-07 covers the sailing; "freight prepaid" agrees with CIF and the bill of lading's prepaid freight at Lumeport.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/TransportServiceDescription/cac:Signature/cbc:ID` = `TWL-SIG-TSD`: prefix `TWL` differs from the document prefix `TOL` — refuted: `TWL` is the same carrier's code (its container prefix `TWLU`) (from broad).
- `/TransportServiceDescription/cac:TransportationService/cbc:SequenceNumeric` = `1` for a single service — refuted: 1 is the first of a sequence (from broad).
- `/TransportServiceDescription/cac:ServiceChargePaymentTerms/cbc:Note`: freight prepaid before release of the bill of lading — refuted: an ordinary liner condition, consistent with CIF (from context).
- `/TransportServiceDescription/cac:TransportationService/cac:TransportEquipment/cbc:SizeTypeCode`: 42G1 both as equipment and as supported equipment — refuted: proposed equipment vs accepted types (from context).

## Changed in the merge
- context/F2 (Medium, event + weekday) split: the weekday part grouped with broad/F2 and logistics/F2 into F2 (High, with context's cut-off reading carried), the untyped-event part with broad/F3 and logistics/F4 into F8.
- broad/F5, parties/F1, context/F5 → F4: preferred option drop, aligned.
- context/F9 → F5: Low raised to Medium, aligned.
- F9 (signature) added in the merge, aligned with 01#F6, 07#F5 and earlier flows.
- context/F8 → F10: extended with Lumeway's customs-trader number.
- broad/F7, logistics/F6, context/F6 → F13: grouped; the dependence of the per-tonne-km check on F3 noted.

## Outside this review
- The description is issued on Saturday 2026-05-09 and `12-ForwardingInstructions.xml` on Sunday 2026-05-10, while the digital agreement's SLA has the network available Monday to Friday only (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalAgreementTerms/cac:ServiceLevelAgreement/cbc:SaturdayAvailabilityIndicator` = `false`) and all contacts work "Weekdays 08:00–17:00": a timeline question across documents (from broad).
- `15-Manifest.xml` estimates the departure on 2026-05-15 while `13-TransportationStatus.xml` reports the actual departure on 2026-05-14: for the reviews of those examples.
