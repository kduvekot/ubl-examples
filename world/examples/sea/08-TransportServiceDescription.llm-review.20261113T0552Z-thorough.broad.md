# LLM review: 08-TransportServiceDescription.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/08-TransportServiceDescription.xml`, Git blob `3b64d9a508af69f9f2be5711a0061f17a39e8741` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/08#F1 · High · Booking deadline already past when the service is offered
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationDate` = `2026-05-09`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationTime` = `10:00:00`
- XPath: `/TransportServiceDescription/cbc:IssueTime` = `12:03:00`
- Why: `NominationDate`/`NominationTime` are "the deadline date [time] by which this transportation service has to be booked". The description is issued on 2026-05-09 at 12:03, two hours after that deadline, and offers the service (`ResponseCode` `OFFERED`). Lumeway could not book it in time; yet the flow books it afterwards (`12-ForwardingInstructions.xml`, issued 2026-05-10).
- Condition: the nomination deadline is after the issue of the description and before (or at) the booking the flow makes.
- Options: (a) preferred: a nomination deadline after 2026-05-10 09:15 and before the cargo acceptance on 2026-05-13 (e.g. 2026-05-12); (b) none better seen.
- Needs decision: no

### sea/08#F2 · High · Sailing on a Thursday, but the service runs on Fridays
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: `ScheduledServiceFrequency` gives the day of the week "a transport service is operational": `5`, Friday. The only event of the service is on 2026-05-14, a Thursday (calendar). The weekly feeder cannot sail on a day it does not operate.
- Condition: the day of the service's event is the scheduled weekday (or the schedule lists that weekday).
- Options: (a) preferred: WeekDayCode `4` (Thursday), if the flow's sailing on 2026-05-14 is right; (b) move the event to a Friday (which changes the flow's dates).
- Needs decision: no

### sea/08#F3 · Medium · Transport event without type or location
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`
- Why: the event has a date, a time and "not completed", but neither a `TransportEventTypeCode` nor a `Location`: the reader cannot tell whether 18:00 is the departure from Lumeport, the closing time for cargo or the arrival. For a service description the next departure is what the shipper needs.
- Condition: the event says what happens (type) and where (location).
- Options: (a) preferred: type "departure" (or the dedicated code of the world's event list) with Lumeport (`XBLMP`) as location; (b) none better seen.
- Needs decision: no

### sea/08#F4 · Medium · A goods classification as classification of the transport service
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:CommodityClassification/cbc:ItemClassificationCode` = `38111`
- Why: under `TransportationService`, `CommodityClassification` is "A classification of this transportation service". CPC 38111 "Seats, primarily with metal frames" classifies Lumeway's benches, not a liner service; the goods a service can take are stated in `SupportedCommodityClassification` (here `GEN`). A service would be classified by a CPC service class for freight transport by sea (CPC division 65, own knowledge), or not at all. The description is also a general offer ("Our island service."), not tied to one cargo.
- Condition: the service's `CommodityClassification` classifies the service, or is absent.
- Options: (a) preferred: drop it; (b) a CPC code for coastal/transoceanic freight transport services.
- Needs decision: no

### sea/08#F5 · Medium · Language code in LocaleCode
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/08#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/08#F7 · Low · Emission of the service without what it applies to
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EnvironmentalEmission/cbc:ValueMeasure` = `380`
- Why: 380 kg CO2e is stated for "this transportation service" with no base (per container, per TEU, per voyage), no method and no description. For a whole two-day feeder voyage of a 1,000 TEU ship it is far too low (own estimate: tens of tonnes); per 40-foot box it is plausible. Without a base the figure cannot be used.
- Condition: the emission states its base (e.g. `ValueFactorNumeric` with `ValueBaseMeasure` per container) or its scope in a description.
- Options: (a) preferred: per container: factor 380 kg per 1 container (40 ft) with a short method; (b) drop it.
- Needs decision: no

### sea/08#F8 · Low · Lumeway's sales customer service as receiver of a carrier's offer
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the carrier answers Lumeway's request for a transport service; its contact should be the function that books transport, not Sales' customer service (same contact as in `07-TransportServiceDescriptionRequest.xml`).
- Condition: the receiver's contact arranges transport.
- Options: (a) preferred: a shipping/logistics contact of Lumeway.
- Needs decision: no

## Checked and consistent
- The request reference resolves to `07-TransportServiceDescriptionRequest.xml` (`LD-DOC-26-0129`); the answer covers what was asked (weekly sailing to Selanu, container liner).
- The equipment fits: the flow ships one 42G1 (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:SizeTypeCode` = `42G1`), which the service supports; general cargo supported, bulk and reefers not.
- Two days at sea agrees with the description text and `EstimatedDurationPeriod`; validity 2026-05-09 to 2026-08-07 covers the flow's shipment; "freight prepaid" agrees with the bill of lading's prepaid freight at Lumeport (`FreightChargeLocation` `XBLMP`).
- Unit code `20` (twenty foot container) fits a TEU capacity; 1,000 TEU is plausible for a feeder.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/TransportServiceDescription/cac:Signature/cbc:ID` = `TWL-SIG-TSD`: prefix `TWL` differs from the document prefix `TOL` — refuted because signature IDs are free identifiers and `TWL` is the same carrier's code (its container prefix in the flow is `TWLU`).
- `/TransportServiceDescription/cac:TransportationService/cbc:SequenceNumeric` = `1`: a sequence number for a single service — refuted because the definition allows ordering services in a sequence, and 1 is the first.

## Outside this review
- Timeline across documents: this description is issued on a Saturday (2026-05-09) and `12-ForwardingInstructions.xml` on a Sunday (2026-05-10), while the digital agreement's SLA has the network available Monday to Friday only (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalAgreementTerms/cac:ServiceLevelAgreement/cbc:SaturdayAvailabilityIndicator` = `false`) and all contacts work "Weekdays 08:00–17:00".
