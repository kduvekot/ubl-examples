# LLM review: 07-OrderChange.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/07-OrderChange.xml`, Git blob `220443693fcba6ab4d358a9dfcb03af2a2d47f07` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### modification/07#F1 · Low · The buyer's contact is the sawmill's sales office
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: As 01#F2. Here the call-off concerns the sawmill's sale to Valdara, so a sales contact is more defensible than in 01, but the contact is that of the buyer of the processing job.
- Condition: Marrowdale's buyer contact is the same as in 01 and fits the role.
- Options: follow 01#F2.
- Needs decision: no

## Checked and consistent
- `/OrderChange/cac:OrderReference/cbc:ID` = `MDS-PO-26-0047` resolves to 01; SalesOrderID agrees; SequenceNumberID 1 is the first change.
- The call-off fits 01's note ("hold the bundles in your store until we call them off"); 96 bundles agree with 01 and 06.
- 2026-02-26 is a Thursday, as the note says; despatch and delivery date agree with 08's issue and tax point date.
- `/OrderChange/cac:DeliveryTerms/cbc:LossRiskResponsibilityCode` = `BUYER` agrees with FCA and with the text "at the sawmill's risk from the moment they are loaded" (the sawmill is the buyer).
- Pallets: 96 bundles at four to a pallet = 24 pallets, the "bay of 24 pallet places" billed in 08.
- Physics: a bundle of 50 slats 1.8 × 0.095 × 0.045 m is 0.385 m³; 96 bundles are 36.9 m³ and, at 212.5 kg a bundle (wood/06-DespatchAdvice.xml), about 20.4 t plus pallets: within a curtain-side semi-trailer's payload of about 24 t (own knowledge).
- Valdara Industries' identifiers agree with the other examples carrying it (`0990:10014`, 81 occurrences over `*.xml`).

## Considered and refuted
- `/OrderChange/cac:Delivery/cac:Despatch/cbc:Instructions`: the processor is asked to send the despatch advice to Valdara on the sawmill's behalf — refuted as a problem: a plausible arrangement for goods held in a third party's store.
