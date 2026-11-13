# LLM review: 07-TransportServiceDescriptionRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/07-TransportServiceDescriptionRequest.xml`, Git blob `4ae3dd59b6e90f59d04287ec02b7468d52e39968` (committed)
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

### sea/07#F1 · Medium · Language code in LocaleCode
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/07#F2 · Medium · A gate in AdditionalStreetName
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/07#F3 · Low · The route of the requested service only in a note, without an origin
- XPath: `/TransportServiceDescriptionRequest/cbc:Note` = `Weekly sailings to Selanu, please.`
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: the request asks for a description of a container liner service; the only structured statement is the service code. The destination is in free text and the port of loading is not stated at all, although the answer depends on both (the description that comes back states the route `08-TransportServiceDescription.xml`). `TransportationService` can carry the route (e.g. `TransportEquipment`, `SupportedTransportEvent` locations, `ShipmentStage`).
- Condition: the requested service states where from and where to in structured form (e.g. load and discharge locations), consistent with the note.
- Options: (a) preferred: add the route Lumeport–Selanu to the transportation service; (b) at least name the port of loading in the note.
- Needs decision: no

### sea/07#F4 · Low · Sales customer service asks for a transport service
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender's contact is the point the carrier answers to about sailings and bookings; Lumeway's customer service in Sales is its contact for buyers. A transport user's contact for a carrier is its shipping or logistics function.
- Condition: the sender's contact is a function that arranges transport, or the document explains why Sales does.
- Options: (a) preferred: a shipping/logistics contact of Lumeway (as the forwarding instructions would need too); (b) none better seen.
- Needs decision: no

## Checked and consistent
- Sender Lumeway and receiver/transport service provider Tidewell Ocean Lines (ISIC 5012, sea freight) are the right parties; Tidewell's contact "Bookings", operations planner in Operations, fits a carrier.
- Issued 2026-05-08 14:00, after the order response of 09:30 that confirms CIF (the seller arranges carriage); the answer `08-TransportServiceDescription.xml` references this request (`LD-DOC-26-0129`).
- GLN check digit correct (`check_ids.py`).
