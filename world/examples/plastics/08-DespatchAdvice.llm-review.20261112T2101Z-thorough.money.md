# LLM review: 08-DespatchAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/08-DespatchAdvice.xml`, Git blob `40cea0e7c3b5f742441038658c674f3f93c6cc68` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### plastics/08#F1 · Low · Delivery customer's bank account in a despatch advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". A despatch advice announces goods; it carries no amounts, payment means or terms, and the receiving party's current account is used by nothing in it. It is copied master data. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the despatch advice carries no party financial account.
- Options: (a, preferred) drop it.
- Needs decision: no

## Checked and consistent
- The despatch advice carries no prices or values; the goods invoice that references it (`10-Invoice.xml:/Invoice/cac:DespatchDocumentReference/cbc:ID` = `RR-DA-26-0892`) bills the 120 t announced here.
