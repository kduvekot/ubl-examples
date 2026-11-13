# LLM review: 07-TransportServiceDescriptionRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/07-TransportServiceDescriptionRequest.xml`, Git blob `4ae3dd59b6e90f59d04287ec02b7468d52e39968` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit f2df446 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/07#F1 · Medium · LocaleCode holds a language code (two places)
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; both hold the ISO 639 language code already in `Language/ID`, so neither names a locale. 362 such elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: each `LocaleCode` is absent or a locale (language with region) from a locale list.
- Options: (a) preferred: drop them; (b) `en-XB` from a list of language tags.
- Needs decision: no
- From: broad (F1), parties (F1), context (F2)

### sea/07#F2 · Medium · A gate in AdditionalStreetName of the sender's postal address
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name and has no use in a postal address. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F2), parties (F2), context (F5, Low)

### sea/07#F3 · Medium · A kind of service in the element for the extent of the service
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: `TransportServiceCode` is "A code signifying the extent of this transportation service (e.g., door-to-door, port-to-port)". The world list's code means "Container liner service", a mode and kind of service, not an extent; whether Lumeway wants port-to-port or door-to-door (under CIF Selanu, port-to-port) is not said. A code whose meaning is not the one the definition names (section 6, Medium).
- Condition: `TransportServiceCode` holds an extent (e.g. port-to-port) from a list of extents; the container liner character is given where UBL has an element for it (service name, description, transport mode).
- Options: (a) preferred: an extent code (port-to-port) and the liner/container character in `Name` or the transport mode; (b) redefine the world list so that its codes are extents.
- Needs decision: no
- From: context (F1)

### sea/07#F4 · Medium · The request does not say between which places, for which cargo or which equipment
- XPath: `/TransportServiceDescriptionRequest/cbc:Note` = `Weekly sailings to Selanu, please.`
- XPath: `/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `OCEANCONT`
- Why: the document is "A document requesting a Transport Service Description, sent from a party with a transport demand"; its `TransportationService` is "A transportation service about which information is requested". The only structured statement of the demand is the service code; the destination is in free text, the origin (Lumeport) and the cargo or equipment are not stated at all. The answer nevertheless offers a specific route, commodity and container type (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cbc:TransportationServiceDescription` = `A weekly feeder sailing from Lumeport to Selanu, two days at sea.`), information the carrier could only have from outside this request. Medium (information the purpose depends on; the checklist names "a transport request that does not say what is to be carried"), not Low as broad and context had it.
- Condition: the request states, in structured elements, at least origin and destination and what is to be carried (commodity, cargo type or wanted equipment), consistent with what 08 answers.
- Options: (a) preferred: the route Lumeport (`XBLMP`) – Selanu (`XLSEL`) in the transportation service's structure (e.g. a shipment stage with load and unload locations), the benches' commodity classification and the wanted equipment `42G1`; (b) at least name Lumeport and the equipment in the note; (c) reduce the answer to what was asked.
- Needs decision: no
- From: logistics (F1), broad (F3, Low), context (F3, Low)

### sea/07#F5 · Low · Signature with only an ID and a signatory, on an information request
- XPath: `/TransportServiceDescriptionRequest/cac:Signature/cbc:ID` = `LD-SIG-TSDR`
- XPath: `/TransportServiceDescriptionRequest/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the signature has no method, attachment or validation; nothing is signed. The context part refuted a signature on a mere information request (signing outgoing documents can be a party's policy; it contradicts nothing); that answers whether a signature may be here, not whether this one is a signature. 137 of the 147 `Signature` aggregates of the world hold only `ID` and `SignatoryParty` (lxml count over `world/examples/*/*.xml`); earlier merges kept this as Low/yes (see 01#F6).
- Condition: either the signature carries what makes it one (method, attachment or reference), or the request has no `Signature`; one rule across the world.
- Options: (a) preferred: drop it; (b) document the convention.
- Needs decision: yes (world-wide convention)
- From: context (Considered and refuted); made a finding in the merge, aligned with earlier flows

### sea/07#F6 · Low · Legal and tax master data of both parties in an information request
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `/TransportServiceDescriptionRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: a request for a service description commits to nothing and has no tax, legal or customs effect; the carrier's share capital, size and tax number, and Lumeway's own tax scheme, legal entity and customs-trader number play no role in it (section 4.8). `CorporateStockAmount` is defined as "The number of shares" though typed as an amount (TC write-up note, not a finding here).
- Condition: sender and receiver carry identification, name, contact and endpoint only, or the request has a reason for the rest.
- Options: (a) preferred: reduce both parties.
- Needs decision: no
- From: context (F4); the customs-trader number and sender's tax scheme added in the merge (same kind of data)

### sea/07#F7 · Low · The transport user's contact is its sales customer service
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportServiceDescriptionRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway asks a carrier about sailings as a transport user; the carrier answers the function that books transport (shipping, despatch, logistics), not the sales customer service that serves Lumeway's buyers (checklist: a contact fits the party's role in the document). The carrier's own contact (Bookings, operations planner in Operations) fits.
- Condition: the sender's contact is a function that arranges transport, or absent.
- Options: (a) preferred: a shipping/logistics contact for Lumeway's transport roles; (b) no contact in transport documents where nobody needs to reach Lumeway about the shipment.
- Needs decision: no
- From: broad (F4), parties (F3), context (F6)

## Checked and consistent
- Sender and signatory Lumeway (transport user); receiver and transport service provider Tidewell Ocean Lines (`20411918`, ISIC 5012, sea freight), described identically in all full renderings of the flow (parties).
- `ServiceInformationPreferenceCode` "Schedule first" agrees with the note asking for weekly sailings.
- Issued 2026-05-08 14:00, after the order response (09:30) that confirms CIF Selanu (the seller arranges carriage); answered by 08-TransportServiceDescription.xml, which references `LD-DOC-26-0129` and is issued the next day.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/TransportServiceDescriptionRequest/cac:Signature/cbc:ID`: a signature on an information request — refuted by context (policy); not followed for the signature's form, see F5.

## Changed in the merge
- broad/F1, parties/F1, context/F2 → F1: preferred option drop, aligned.
- context/F5 → F2: Low raised to Medium, aligned.
- logistics/F1 (Medium) + broad/F3 (Low) + context/F3 (Low) → F4: Medium.
- context's refutation of the signature → F5 (Low/yes), aligned with 01#F6 and earlier flows.
- context/F4 → F6: extended with Lumeway's tax scheme and customs-trader number.
