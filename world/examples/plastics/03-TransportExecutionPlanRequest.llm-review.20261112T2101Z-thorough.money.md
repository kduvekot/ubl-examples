# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/03-TransportExecutionPlanRequest.xml`, Git blob `ce4cb0e21e72b3398e1856fda182f568fe87940d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/03#F1 · Low · Consignee's bank account in a transport request
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". The consignee Rivermouth neither pays nor receives anything under this transport request: the transport is billed to Rinova (`/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`), consistent with `CPT` in the order. The consignee's current account is master data copied into a document that does nothing with it. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the consignee party in the request carries no financial account unless the request uses it (e.g. freight collect from the consignee).
- Options: (a, preferred) drop the `FinancialAccount` from the consignee party; (b) keep it only if the story makes the consignee pay part of the transport.
- Needs decision: no

## Checked and consistent
- `BillToParty` = Rinova Recovery, the seller under `CPT`, who also receives the freight invoice (`07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`).
