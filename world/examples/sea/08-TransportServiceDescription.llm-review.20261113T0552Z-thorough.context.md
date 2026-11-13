# LLM review: 08-TransportServiceDescription.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/08-TransportServiceDescription.xml`, Git blob `3b64d9a508af69f9f2be5711a0061f17a39e8741` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0919fae 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/08#F1 · High · Booking deadline passed before the service description was issued
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationDate` = `2026-05-09`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationTime` = `10:00:00`
- XPath: `/TransportServiceDescription/cbc:IssueTime` = `12:03:00`
- Why: NominationDate/Time is "the deadline … by which this transportation service has to be
  booked". The description announcing the service was issued on 2026-05-09 at 12:03, two hours
  after that deadline; the booking that follows in the flow (the forwarder's instructions to the
  carrier, `12-ForwardingInstructions.xml`, issued 2026-05-10) comes a day after it. A service
  offered with a deadline already passed cannot be booked.
- Condition: the nomination deadline lies after the issue of the description and no later than the
  cargo cut-off of the sailing it refers to, and after it the booking in the flow is on time.
- Options: (a) preferred: a deadline before the 15 May sailing (e.g. 2026-05-12), after the
  booking of 12-ForwardingInstructions; (b) drop the nomination deadline from a general service
  announcement.
- Needs decision: no

### sea/08#F2 · Medium · Transport event without type or place, on a day the service does not sail
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`
- Why: TransportEvent is "one or more transport events taking place in this transportation
  service"; this one has neither an event type nor a location, so it says nothing. 2026-05-14 is a
  Thursday, while the service sails on Fridays (WeekDayCode 5); the manifest has the departure on
  Friday 15 May (`15-Manifest.xml`). The event is probably the cargo cut-off for that sailing, but
  the document does not say so.
- Condition: the event has a type code (and location) that says what happens at 2026-05-14 18:00,
  consistent with a Friday sailing, or it is removed.
- Options: (a) preferred: type it as the cargo/gate cut-off at the Lumeport terminal; (b) replace it
  by the next departure (Friday) as a typed event.
- Needs decision: no

### sea/08#F3 · Medium · The service classified with a goods code for seats
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:CommodityClassification/cbc:ItemClassificationCode` = `38111`
- Why: In TransportationService, CommodityClassification is "a classification of this
  transportation service". CPC 38111 "Seats, primarily with metal frames" classifies goods, not a
  transport service (CPC has service classes for coastal and transoceanic freight). The general
  feeder service is announced as freight-all-kinds for general cargo (TariffClassCode FAK,
  SupportedCommodityClassification GEN); a goods code of the benches does not classify it.
- Condition: the service's CommodityClassification holds a service classification, or is absent;
  the cargo the request concerned may appear as supported commodities.
- Options: (a) preferred: drop it (the supported/unsupported cargo types already say what the
  service carries); (b) a CPC service code for coastal container freight.
- Needs decision: no

### sea/08#F4 · Medium · A kind of service in the element for the extent of the service
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: TransportServiceCode is "a code signifying the extent of this transportation service (e.g.,
  door-to-door, port-to-port)"; "container liner service" is a kind of service.
- Condition: an extent code (e.g. port-to-port), the kind given elsewhere.
- Options: (a) preferred: port-to-port, since the description is a sailing Lumeport–Selanu.
- Needs decision: no

### sea/08#F5 · Medium · A language code in LocaleCode (two places)
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; both are the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/08#F6 · Low · Emission of the service without a base
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EnvironmentalEmission/cbc:ValueMeasure` = `380`
- Why: The emission is "an environmental emission resulting from this transportation service". A
  two-day feeder sailing with a 1,000 TEU capacity (stated in the same service) emits in the order
  of 150–200 t CO2 (own estimate: some 25–30 t of fuel a day at about 3.1 t CO2 per t of fuel);
  380 kg fits one 40 ft container's share (about 190 kg per TEU), not the service. Without
  ValueFactorNumeric/ValueBaseMeasure or a description, the reader cannot tell what the 380 kg
  refers to.
- Condition: the emission states its base (per container, per TEU or per voyage), and the value fits
  that base.
- Options: (a) preferred: a factor per FEU/TEU with its base, or a description "per 40 ft
  container"; (b) drop it.
- Needs decision: no

### sea/08#F7 · Low · Shipper's contact for a transport offer is its sales customer service
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway receives the carrier's offer as a transport user; the contact who handles shipping is
  a logistics or shipping function, not sales customer service (which serves Lumeway's own buyers).
- Condition: the receiver's contact is the function that books transport, or the contact is absent.
- Options: (a) preferred: a shipping/logistics contact of Lumeway.
- Needs decision: no

### sea/08#F8 · Low · Legal and tax master data of both parties in a service announcement
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: The announcement has no legal or tax effect; share capital, tax numbers and registrations of
  both parties play no role. Looks copied from master data.
- Condition: Sender and Receiver carry identification, name, contact and endpoint only.
- Options: (a) preferred: reduce both parties.
- Needs decision: no

### sea/08#F9 · Low · A gate in AdditionalStreetName of the receiver's postal address
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name": a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it, or move it to a pickup location where the carrier collects.
- Needs decision: no

## Checked and consistent
- TransportServiceDescriptionRequestDocumentReference `LD-DOC-26-0129` resolves to
  07-TransportServiceDescriptionRequest (sender and receiver swapped, as expected).
- Duration two days agrees with "two days at sea"; the manifest's departure 15 May and arrival
  17 May (15-Manifest) fit it and the Friday sailing day.
- Capacity 1,000 TEU (unitCode 20) with AttributeID TEU is consistent; 42G1 used and supported,
  22G1 supported, 45R1 reefer unsupported; general cargo supported and dry bulk unsupported fit a
  dry container feeder.

## Considered and refuted
- `/TransportServiceDescription/cac:ServiceChargePaymentTerms/cbc:Note`: freight prepaid before
  release of the bill of lading — refuted: an ordinary liner payment condition, consistent with CIF
  (the seller pays freight).
- `/TransportServiceDescription/cac:TransportationService/cac:TransportEquipment/cbc:SizeTypeCode`:
  TransportEquipment and SupportedTransportEquipment both carry 42G1 — refuted: the first is the
  equipment used (proposed) for this demand, the second what the service accepts.
