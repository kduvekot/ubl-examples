# LLM review: 04-TransportProgressStatusRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/04-TransportProgressStatusRequest.xml`, Git blob `1fc0afc119b31bbce07b12c53077e4e7f9cd7e51` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0cafa9c 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### rail/04#F1 · Medium · Province given in Region
- XPath: `/TransportProgressStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, which UBL puts in CountrySubentity ("such as the name of its county, province, or state"). 219 occurrences over the examples (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: An administrative province is in CountrySubentity; Region only for a non-administrative region.
- Options: (a) preferred: CountrySubentity; (b) keep Region if the world defines provinces as non-administrative.
- Needs decision: yes (a fact of the world)

### rail/04#F2 · Low · Terminal control reachable only in office hours
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/TransportProgressStatusRequest/cbc:IssueTime` = `06:30:00`
- Why: The hub's terminal control is asked about a container train due out at 06:45 (03) and answers at 06:45 (05); a terminal control that works trains before 07:00 is not plausibly reachable only on weekdays from 08:00 to 17:00. Contact/Note is "a textual description of the circumstances under which this contact can be used".
- Condition: The terminal control's availability covers the hours in which the flow uses it.
- Options: (a) preferred: hours that fit a terminal (e.g. "Round the clock" or the hub's shift times); (b) drop the Note.
- Needs decision: no

## Checked and consistent
- The request is answered by 05 (`05-TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportProgressStatusRequestDocumentReference/cbc:ID` = `FRC-DOC-26-0329`), from the receiver back to the sender; the journey CT 4471 and the status location are the same.
- The journey CT 4471 is the one planned in 03 and carried on the waybill (08).
- Parties (Ferrano Rail Cargo as sender and signatory, Ferrano Intermodal Hub as receiver) are described as in the other rail examples.

## Considered and refuted
- `/TransportProgressStatusRequest/cac:TransportMeans/cbc:JourneyID` = `CT 4471`: suspected too little to identify the transport means — refuted because a scheduled journey identifies the train for the hub; nothing more is needed to ask for its status.
- `/TransportProgressStatusRequest/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: suspected the same availability problem as the hub's — refuted because the request is a system message of the carrier; its freight desk does not need to be reachable at 06:30.

## Outside this review
- Timeline: the request "Has the container train left?" (`/TransportProgressStatusRequest/cbc:Note[2]` = `Has the container train left?`) is sent at 06:30, a quarter of an hour before the planned departure at 06:45 (03); whether asking that early is plausible is a question of the flow's timeline.
