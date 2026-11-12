# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/03-Waybill.xml`, Git blob `bd3a3f9d377d18d732a5834ff59fed7e413de940` (committed)
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
- `/Waybill/cac:Shipment/cac:Consignment`: suspected that an air waybill should state its charges and whether they are prepaid or collect (the document has no amount, charge or payment terms at all) — refuted because the UBL definition of the Waybill says it "may contain" charges, and the flow does not bill the carriage: the seller pays it under `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT` and contracts the forwarder, who is the waybill's receiver (`/Waybill/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`). Nothing in the flow contradicts this; a whoever-pays statement would only become necessary if a freight invoice were added.
