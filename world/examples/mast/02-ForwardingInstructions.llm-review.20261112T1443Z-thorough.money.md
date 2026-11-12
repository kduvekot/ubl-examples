# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/02-ForwardingInstructions.xml`, Git blob `2697645dcfc391cd36edbe8e8ed4c28f35be7a85` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment`: suspected that the instructions should say who pays the forwarder's and the airline's charges (no payment terms, freight charge or prepaid/collect indication anywhere in the document) — refuted because the forwarding instructions are given by the consignor, Saltmere Engineering (`/ForwardingInstructions/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`), who is the forwarder's customer and, under the sale's delivery terms `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT`, the party that pays the carriage; the UBL document does not require the charges, and the absence carries no other meaning in this flow. A later forwarder invoice is not part of the flow.
- `/ForwardingInstructions/cac:ConsignorParty/cac:PartyTaxScheme` and `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyTaxScheme`: suspected tax registrations without a tax use — the forwarder will bill the consignor for its service, so both registrations have a reason here; whether they are needed otherwise is for the parties lens.
