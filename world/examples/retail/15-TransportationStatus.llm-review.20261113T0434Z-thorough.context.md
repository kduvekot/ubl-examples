# LLM review: 15-TransportationStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/15-TransportationStatus.xml`, Git blob `5b9a4c32822b9c4f60e917122105de36cde607f1` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/15#F1 · High · The carrier's own shipment reference differs from the waybill's
- XPath: `/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- Why: CarrierAssignedID is "A reference number assigned by a carrier or its agent to identify a
  specific shipment". Bayforth assigned `BF-CMR-26-0217` to this shipment on its waybill; in its own
  status report it gives `BF-ROAD-26-0231`, and the request it answers gave yet another value. One
  shipment, three carrier references.
- Condition: the status report carries the same carrier reference as the waybill.
- Options: `BF-CMR-26-0217` (preferred).
- Needs decision: no

### retail/15#F2 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/15#F3 · Low · Status type "current" in answer to a request for delivery status
- XPath: `/TransportationStatus/cbc:TransportationStatusTypeCode` = `CURRENT`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:TransportationStatusTypeCode` = `DELIVERY`
- Why: the request asks for the "Status of delivery" ("Answer with the expected delivery time"); the
  report's main content is the updated delivery event. Its type code says "Current status".
- Condition: the type code matches the status the report gives, i.e. the one requested.
- Options: `DELIVERY` (preferred), or keep `CURRENT` if the position report is meant as the main
  content.
- Needs decision: no

### retail/15#F4 · Low · A position report as an untyped event without time
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Marrowdale ring road`
- Why: TransportEvent is "Any additional events associated with this Transportation Status report
  that are not defined elsewhere in this document". The event has no type code and no time, only a
  date; its description repeats the expected arrival that the UpdatedDeliveryTransportEvent already
  gives. The reader cannot tell when the truck was on the ring road.
- Condition: the event has a type (en route / position) and a time, and its description does not
  restate the delivery update.
- Options: add TransportEventTypeCode and OccurrenceTime, shorten the description (preferred).
- Needs decision: no

## Checked and consistent
- TransportationStatusRequestDocumentReference `LD-DOC-26-0232` resolves to
  14-TransportationStatusRequest.xml, issued 50 minutes earlier; sender Bayforth and receiver Lumeway
  are the request's receiver and sender.
- The consignment `LD-CS-26-0228` is the one of 11 to 14.
- UpdatedDeliveryTransportEvent ("Update of the original plan regarding a delivery") at 14:00 the same
  day is in the future relative to the issue time 11:49, as an expected time must be.

## Outside this review
- The expected arrival on 2026-04-29 at 14:00 against the receipt on 2026-04-30 at 10:40
  (17-ReceiptAdvice.xml) and the despatch advice issued at 15:34 on the 29th (12-DespatchAdvice.xml),
  after the expected arrival: a timeline question across the flow.
