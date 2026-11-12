# LLM review: 05-Waybill.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/05-Waybill.xml`, Git blob `e7a36055c2d576e9c4683563c6c0c9a29856e375` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: checked against the definition ("A term used in commerce in reference to certain duties, called ad valorem duties, which are levied on commodities at certain rates per centum on their value"): a domestic rail carriage within Urvania bears no ad valorem duty and the freight is per tonne (06-Invoice.xml), so `false` is correct — no finding.
- The consignment note states no freight charges or who pays them, although the Waybill definition mentions "charges" — refuted: the elements are optional, the bill-to party is fixed in the transport plan (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Valdara Industries`) and FCA terms (01-Order.xml) make the buyer pay; the freight invoice 06-Invoice.xml bills Valdara accordingly.
- `/Waybill/cbc:IssueDate` = `2026-03-10` is the start of the 30-day freight payment term agreed in the transport plan; the freight invoice does not follow it — recorded as a finding of 06-Invoice.xml, not here.
