# LLM review: 06-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/06-Invoice.xml`, Git blob `b3fee4995e687ca616a88364c0b3bc9ec2261466` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### ore/06#F1 · High · Bulk-wagon freight billed under a plan for a container train
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- Why: the invoice bills rail freight for ore in bulk wagons and refers to the transport execution
  plan, but that plan's main service is `RAILCONT`, "Containers on a scheduled container train"
  (also in 02-TransportExecutionPlanRequest.xml). The invoice and the plan it refers to describe two
  different services. The invoice's description fits the rest of the flow (loose ore, 30 wagons);
  the wrong value is most likely the plan's.
- Condition: the service billed and the main transportation service of the referenced plan describe
  the same kind of carriage.
- Options: (a, preferred) correct the plan (and request) to a wagon-load service, leaving this
  invoice as it is; (b) none other sensible: the goods are not in containers.
- Needs decision: no

### ore/06#F2 · Low · Additional references with only an ID
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`
- Why: both resolve (03-TransportExecutionPlan.xml, 05-Waybill.xml), but an additional document
  reference is generic and neither says what it is (no `DocumentTypeCode` or `DocumentType`); the
  receiver can tell only from the number prefixes that one is the transport plan and the other the
  consignment note that proves the carriage. 555 of 595 document references in the examples carry
  only an ID (lxml over `*/*.xml`).
- Condition: each additional reference states the type of the referenced document.
- Options: (a, preferred) `DocumentTypeCode` (world UBLDocumentTypeCode `TransportExecutionPlan`,
  `Waybill`) on both; (b) `DocumentType` text.
- Needs decision: no

## Checked and consistent
- Quantity: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `1788.4` t equals the waybill's
  weight (1 788 400 kg in 05-Waybill.xml) and the despatched quantity (04-DespatchAdvice.xml).
  1788.4 × 962 = 1 720 440.8, rounded to the line amount 1 720 441.
- References resolve: `FRC-TEP-26-0307` → 03-TransportExecutionPlan.xml, `FRC-WB-26-0310` →
  05-Waybill.xml; carrier/supplier and customer agree with both (Valdara is bill-to party in 03).
- Times: issued 2026-03-12 14:45, after the waybill (2026-03-10) and within the service window
  (to 2026-03-13).
- Line description "Ore from the mine siding to the factory siding, per tonne" fits the plan's from and
  to locations.

## Outside this review
- The flow records no arrival time, so whether the plan's bonus (delivery on the first day) or penalty
  should appear on this invoice cannot be decided from the documents (timeline across documents).
