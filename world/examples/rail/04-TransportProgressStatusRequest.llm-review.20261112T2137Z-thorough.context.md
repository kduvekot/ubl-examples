# LLM review: 04-TransportProgressStatusRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/04-TransportProgressStatusRequest.xml`, Git blob `1fc0afc119b31bbce07b12c53077e4e7f9cd7e51` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/04#F1 · Medium · Province in Region
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is "the political or administrative division of a country" (CountrySubentity), not a "geographic or economic region or group of countries" (Region).
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/04#F2 · Low · The question is asked before the planned departure
- XPath: `/TransportProgressStatusRequest/cbc:IssueTime` = `06:30:00`
- XPath: `/TransportProgressStatusRequest/cbc:Note[2]` = `Has the container train left?`
- Why: The plan has the train leaving at 06:45 (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`). Asking at 06:30 whether it has left makes sense only if the carrier expected an early departure; otherwise the natural question is whether it will leave on time.
- Condition: the question in the note fits the time of the request (asked after the planned departure, or asking about the expected departure).
- Options: (a) preferred: rephrase the note to ask for the expected departure, or (b) issue the request after 06:45.
- Needs decision: no

### rail/04#F3 · Low · Receiver is a terminal operator, the document is addressed to a network manager
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- Why: UBL defines the document as "sent from a transport service provider to a transportation network manager requesting a Transport Progress Status". Ferrano Intermodal Hub is a terminal (ISIC 5221, the terminal operator in rail/07), not the manager of the rail network on which train CT 4471 runs. A terminal can report when the train left its yard, which is what rail/05 does, so the role is a stretch rather than wrong.
- Condition: the receiver is the party that manages the network for which status is requested, or the story says the hub acts as such for its yard.
- Options: (a) preferred: keep the hub and state in the world that it reports departures from its yard for the network; (b) address the request to the rail infrastructure manager, if the world has one.
- Needs decision: yes

## Checked and consistent
- TransportMeans/JourneyID `CT 4471` matches the plan's journey; the status location (the hub) is where the train departs.

## Considered and refuted
- `/TransportProgressStatusRequest/cac:Signature/cbc:ID` = `FRC-SIG-TPSR`: suspected filler — refuted because a signature on a request to another company is a legitimate optional element; no evidence it contradicts anything.
