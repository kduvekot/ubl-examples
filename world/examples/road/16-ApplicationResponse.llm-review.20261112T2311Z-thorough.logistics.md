# LLM review: 16-ApplicationResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/16-ApplicationResponse.xml`, Git blob `1e7f911b472f7aea92ee35fb380bd4e0c2647589` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### road/16#F1 · High · Three-way match passed before the goods arrived or any receipt was recorded
- XPath: `/ApplicationResponse/cbc:ResponseTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.`
- Why: A three-way match compares the invoice with the order and with the goods receipt. The response accepts the invoice on 2026-03-25 at 06:12, but the goods are delivered only at 09:40 that day (`11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cbc:ActualDeliveryTime` = `09:40:00`), the first receipt advice is issued at 15:40 (`11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00`) and reports a bench short, and the corrected receipt is issued only on 2026-03-26 (`13-ReceiptAdvice.xml`). At 06:12 there was no receipt to match; had the match been run against the first receipt, it would have failed on line 1.
- Condition: the response time is after the goods receipt it matches against (after the corrected receipt advice of 2026-03-26 10:48 if the match is to pass on 96 benches).
- Options: (a) preferred: move the response (and its issue date/time) after 2026-03-26 10:48; (b) describe a two-way match (invoice against order) if the buyer accepts before receipt, which changes the note.
- Needs decision: no

## Checked and consistent
- DocumentReference VI-INV-26-0166 resolves to `15-Invoice.xml`; line 2 responded to exists there; IssueTime 12:55 is after the ResponseTime.

## Outside this review
- `/ApplicationResponse/cbc:Note` = `Accepted for payment; line 2 matched the substituted casting.` The goods documents (`04-DespatchAdvice.xml`, `11-`/`13-ReceiptAdvice.xml`, `15-Invoice.xml`) identify line 2 only as VI-C180, without the 2026 version, so the match on "the substituted casting" has nothing to match against; this is a finding in the reviews of those examples.
