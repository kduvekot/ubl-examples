# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/12-WeightStatement.xml`, Git blob `63cbeb9c6ff2202636e981ef15d7262f47f2a1a5` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/12#F1 · Low · Carrier's tax registration and share capital in a weight statement
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: a weight statement is "a document used to report weight or verified mass measurements in
  the transport chain"; this one gives the verified gross mass of one container to the carrier.
  The carrier's Coastal State sales-tax registration and its share capital of 40 000 000 XBL,
  fully paid, play no part in reporting a mass: nothing is billed, taxed or guaranteed by it
  (section 4.8, master data copied into a document that does not use it). The same two blocks
  appear for the carrier in 13 and 14.
- Condition: the weight statement carries a party's tax registration or capital only if reporting
  the mass depends on it.
- Options: (a, preferred) drop the receiver's `PartyTaxScheme`, `CorporateStockAmount` and
  `FullyPaidSharesIndicator`.
- Needs decision: no

## Checked and consistent
- No price, amount, tax or payment information belongs to a verified gross mass; none other is present.
