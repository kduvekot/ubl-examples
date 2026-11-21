# LLM review: 02-OrderResponse.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/02-OrderResponse.xml`, Git blob `a580c76e71fc07eedb1ac2e67fb6b2007f5df9f8` (committed)
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

### modification/02#F1 · Low · The buyer's contact is the sawmill's sales office
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The same contact as in 01 (see 01#F2): Marrowdale Sawmill is the buyer of a processing job, and its sales office is not the desk that buys it.
- Condition: Marrowdale Sawmill's contact as buyer is the same as in the order and fits the buying role.
- Options: follow the fix of 01#F2 (preferred: a purchasing or production-planning contact).
- Needs decision: no

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `MDS-PO-26-0047` resolves to 01-Order.xml; SalesOrderID `TWM-J-2526-014` agrees with 01.
- The note's kiln charges (14–19 and 21–26 January) follow the blank deliveries of 13 and 20 January in 01's note, and the lot dates of the output (`MDS-L26-0119`, `MDS-L26-0126` in 06); "ready in store on 4 February" agrees with 06's AvailabilityDate and lies before 01's LatestDeliveryDate 2026-02-06.
- OrderResponseCode `AP` (accepted) with no line detail: correct for an acceptance without changes.

## Outside this review
- The response (2026-01-13 08:10) is issued at the same minute as the sawmill's despatch advice 03 for the first load; the truck leaves before the acceptance is known. This is a timeline question across documents.
