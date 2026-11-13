# LLM review: 07-TransportServiceDescriptionRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/07-TransportServiceDescriptionRequest.xml`, Git blob `4ae3dd59b6e90f59d04287ec02b7468d52e39968` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/07#F1 · Medium · A kind of service in the element for the extent of the service
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: TransportServiceCode is "a code signifying the extent of this transportation service (e.g.,
  door-to-door, port-to-port)". "Container liner service" names a mode and kind of service, not its
  extent; whether Lumeway wants port-to-port (it delivers to the terminal itself, per the flow's
  pre-carriage) or door-to-door is not said.
- Condition: TransportServiceCode holds an extent (e.g. port-to-port), from a list of extents; the
  kind of service (container liner) is given where UBL has an element for it (e.g. the service's
  transport mode or a description).
- Options: (a) preferred: an extent code (port-to-port) and the liner/container character in
  TransportationService Name or the transport mode; (b) rename the world list so that its codes are
  extents.
- Needs decision: no

### sea/07#F2 · Low · The request does not say between which places, or for what cargo
- XPath: `/TransportServiceDescriptionRequest/cbc:Note` = `Weekly sailings to Selanu, please.`
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: The document requests a Transport Service Description "from a party with a transport demand
  … to a party providing transport services". The service asked about carries only a service code;
  origin (Lumeport) is not stated anywhere, the destination only in the free-text note, and nothing
  says what is to be carried (containers, size). The carrier can answer only by guessing the
  transport demand.
- Condition: the requested service states at least the origin and destination (structured) and the
  kind of equipment, or the note says them.
- Options: (a) preferred: the service's places in the structure the TransportationService offers,
  plus the equipment size; (b) at least name Lumeport in the note.
- Needs decision: no

### sea/07#F3 · Medium · A language code in LocaleCode (two places)
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; both values are
  the ISO 639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/07#F4 · Low · Legal and tax master data of both parties in an information request
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- Why: A request for a service description commits to nothing and has no tax or legal effect; the
  carrier's share capital, size and tax number, and the sender's own legal entity and tax scheme,
  play no role in it. They look copied from master data.
- Condition: Sender and Receiver carry identification, name, contact and endpoint only, or the
  request has a reason for the rest.
- Options: (a) preferred: reduce both parties.
- Needs decision: no

### sea/07#F5 · Low · A gate in AdditionalStreetName of the sender's postal address
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name": a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- Receiver and TransportServiceProviderParty are the same carrier (register ID 20411918); its
  contact (Bookings, operations planner) fits a carrier answering service requests.
- ServiceInformationPreferenceCode "Schedule first" agrees with the note asking for weekly sailings.
- The request (2026-05-08 14:00) is answered by 08-TransportServiceDescription, which references it.

## Considered and refuted
- `/TransportServiceDescriptionRequest/cac:Signature/cbc:ID`: a signature on a mere information
  request — refuted: signing outgoing documents can be a party's policy; it contradicts nothing.
