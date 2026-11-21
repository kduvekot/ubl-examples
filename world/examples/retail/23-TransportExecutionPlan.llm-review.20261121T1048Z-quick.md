# LLM review: 23-TransportExecutionPlan.xml

Flow: retail (LMW-TX-26-0893) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/retail/23-TransportExecutionPlan.xml`, Git blob `d79566499660f6942f32b3a0a4976344e40f8e8f` (committed)
- Last commit changing the example: 99d799b3 2026-11-20 O97 and O78: the call states the withholding, tenders carry the tax subtotal, every time carries its place's UTC offset
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### retail/23#F1 · Medium · Provider's response deadline in the provider's own plan, with a date that differs from the request
- XPath: `/TransportExecutionPlan/cac:TransportServiceProviderResponseRequiredPeriod/cbc:EndDate` = `2026-04-27`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportServiceProviderResponseDeadlinePeriod/cbc:EndDate` = `2026-04-28`
- Why: `TransportServiceProviderResponseRequiredPeriod` "Describes the deadline for when the Transport Service Provider will have to respond to a Transport Execution Plan". This plan is itself the provider's response (sent by Bayforth Forwarding, status `Confirmed`, reason `ASREQUESTED`), so a deadline for the provider to respond has nothing left to govern here. Its date also differs from the deadline the transport user set in the request it answers (28 April): the two documents give two different deadlines for the same response.
- Condition: The plan carries no provider response deadline, or one that agrees with the request's deadline of 2026-04-28 and has a stated purpose.
- Options: (a) preferred: leave the element out of the confirmed plan; the request already set the deadline and the plan, issued on 27 April, met it; (b) keep it with the request's date 2026-04-28, if the plan is meant to echo the request's terms.
- Needs decision: no

### retail/23#F2 · Low · Transport user asked to respond to a plan confirmed as requested
- XPath: `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-28`
- XPath: `/TransportExecutionPlan/cbc:DocumentStatusReasonCode` = `ASREQUESTED`
- Why: `TransportUserResponseRequiredPeriod` "Describes the deadline for when the Transport User will have to respond to a Transport Execution Plan suggested by a Transport Service Provider." The plan does not suggest anything: it confirms the request unchanged (same slot, same service, same consignment as `11-TransportExecutionPlanRequest.xml`). A response deadline for the user fits a plan that proposes changes; for a plain confirmation it asks for an answer nobody needs to give.
- Condition: Either the plan contains something the user must accept (and the deadline stays), or the user response deadline is left out.
- Options: (a) preferred: drop the element from this confirmation; (b) keep it, if the framework contract requires the user to acknowledge every plan (then say so, e.g. in the terms).
- Needs decision: no

## Checked and consistent
- The plan answers `11-TransportExecutionPlanRequest.xml`: same ProfileExecutionID LMW-TX-26-0893, contract LMW-BYF-FW-2026, service FTL, service start 29 April, delivery slot 30 April 10:00–10:30, from/to GLNs 9520610900022 and 9522610900019, consignment LMW-CS-26-0893 with 1 297.2 kg; the plan was issued at 10:30 on 27 April, after the request at 09:10.
- Physics: 24 benches at 12.2 + 13 + 21.8 = 47 kg = 1 128 kg; 6 pallets of 4 benches at 28.2 kg (the pallet weight that results from `rail/14-ImportCustomsDeclaration.xml`) = 169.2 kg; total 1 297.2 kg, as stated.
- The delivery in `15-TransportationStatus.xml` (10:15 at GLN 9522610900019) lies within the confirmed slot; `13-Waybill.xml` and `12-DespatchAdvice.xml` carry the same consignment and weight; payment terms agree with `16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- The waiting-time terms (special terms and service charge terms: 40 lume per hour beyond two hours) agree with each other; all four GLNs pass `check_ids.py`.

## Considered and refuted
- `/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: a full truck load for 6 pallets and 1.3 t — refuted because a dedicated truck (truck B-03, a fixed slot) is a full-load service whatever the fill; the request asked for it.
- `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Delivery slot at the store's goods-in: Thursday 30 April, 10:00 to 10:30. Please confirm by return.`: the user's remarks repeated in the provider's document — refuted: the element holds the transport user's remarks on the operations in the plan, and repeating them shows what was confirmed.

## Outside this review
- `16-Invoice.xml` refers to the request LMW-TR-26-0536 as its order reference and not to this plan; whether that is the right reference belongs to 16's review.
