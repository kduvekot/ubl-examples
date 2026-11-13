# LLM review: 09-DocumentStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/09-DocumentStatusRequest.xml`, Git blob `68cae595b7754cc365ebfdb3b09245cd84b8e2fc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/09#F1 · High · The status reply is issued before this request
- XPath: `/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `/DocumentStatusRequest/cbc:IssueDate` = `2026-04-26`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueDate` = `2026-04-26`
- Why: The document status 10 answers this request ("Has the order been accepted?" / "Accepted and booked.", both about `BS-PO-26-0224`), but it is issued 38 minutes before the request on the same day. A reply cannot precede the request it answers.
- Condition: the request is issued before the status 10 (date and time).
- Options: (a, preferred) move this request before 11:14, or 10 after 11:52; which one depends on the rest of the timeline (10 references the transport request 11 of 2026-04-25 10:28, so either works); (b) the fixing session may choose either side.
- Needs decision: no

## Checked and consistent
- RequestedDocumentReference `BS-PO-26-0224` resolves to the order 08, issued two days earlier by the same sender; TrackingID repeats the order number, which is the business process being tracked.
- The request is issued on 2026-04-26, the last day of the order's validity (`08-Order.xml:/Order/cac:ValidityPeriod/cbc:EndDate` = `2026-04-26`), which gives the question a reason.
