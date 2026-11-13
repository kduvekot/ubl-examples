# LLM review: 10-DocumentStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/10-DocumentStatus.xml`, Git blob `862ae5d80ac13b0164755f867566718b3cc3bf6b` (committed)
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

### retail/10#F1 · High · Status issued before the request it answers
- XPath: `/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `/DocumentStatus/cbc:IssueDate` = `2026-04-26`
- Why: This status replies to the request 09 (both about the order `BS-PO-26-0224`; 09 asks "Has the order been accepted?", this says "Accepted and booked."). Both are dated 2026-04-26, but the reply is 38 minutes earlier than the request.
- Condition: this document is issued after the request 09.
- Options: (a, preferred) issue time after 11:52, e.g. 12:14; (b) move 09 earlier.
- Needs decision: no

### retail/10#F2 · Low · Additional response "accepted" for the distributor's own transport request, which the retailer cannot place
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:DocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:Response/cbc:ResponseCode` = `AP`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: AdditionalDocumentResponse is "A document linked or related to the document for which the status was requested". `LD-TR-26-0227` is the transport execution plan request 11 that Lumeway sent to Bayforth Forwarding; its acceptance would be the forwarder's (a transport execution plan), which the flow does not contain (14 cites a plan `BF-TEP-26-0227` that exists nowhere; see 14/F1). The reference has no type, so the retailer receives an acceptance code for a document ID it has never seen, and the code claims an acceptance that no document in the flow records.
- Condition: the additional response says what `LD-TR-26-0227` is (document type), and its status agrees with what the flow shows about that request (an acceptance only if the forwarder's acceptance exists).
- Options: (a, preferred) give the reference a DocumentType ("Transport booking") and a response description ("Transport booked with the forwarder for 2026-04-29"); (b) drop the additional response, since the retailer only asked about the order.
- Needs decision: no

## Checked and consistent
- DocumentResponse references `BS-PO-26-0224`, the order 08; response code `AP` (UNTDID 4343 "Accepted") agrees with the note "Accepted and booked."
- `LD-TR-26-0227` resolves to 11, issued 2026-04-25 10:28, before this status, so "booked" is possible at the time of this document.
