# LLM review: 07-TransportServiceDescriptionRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/07-TransportServiceDescriptionRequest.xml`, Git blob `4ae3dd59b6e90f59d04287ec02b7468d52e39968` (committed)
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

### sea/07#F1 · Medium · Request does not say between which places, for which cargo or which equipment the service is wanted
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- XPath: `/TransportServiceDescriptionRequest/cbc:Note` = `Weekly sailings to Selanu, please.`
- Why: the document is "A document requesting a Transport Service Description, sent from a party with a transport demand"; its `TransportationService` is "A transportation service about which information is requested". The only structured statement of the demand is the service code "Container liner service"; the destination is in a free-text note, the origin is not stated at all, and neither the cargo nor the equipment is. The answer nevertheless offers a specific route, commodity and container type (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cbc:TransportationServiceDescription` = `A weekly feeder sailing from Lumeport to Selanu, two days at sea.`, commodity `38111` seats and equipment `42G1`), information the carrier could only have from outside this request.
- Condition: the request states, in structured elements, at least the origin and destination (ports or places) and what is to be carried (commodity or cargo type, or the equipment wanted), consistent with what the description in `08-TransportServiceDescription.xml` answers.
- Options: add a shipment stage with loading port `XBLMP` and unloading port `XLSEL`, the commodity classification of the benches and the wanted equipment `42G1` (preferred: the answer then responds to what was asked); or reduce the answer to what was asked.
- Needs decision: no

## Checked and consistent
- Sender and receiver match the roles: Lumeway (transport user) to Tidewell Ocean Lines (transport service provider, same ID `20411918` in both roles); the answer `08-TransportServiceDescription.xml` references this request by its ID `LD-DOC-26-0129` and is issued the next day.
- Issued 2026-05-08 14:00, after the order response (09:30 the same day) that accepted the order CIF Selanu, so the request follows the commitment to ship.
