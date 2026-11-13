# LLM review: 16-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/16-Invoice.xml`, Git blob `e1ce518ac0f84644902623e83922648f889ca0d0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/16#F1 · Low · Transport invoiced nine minutes before the goods were received
- XPath: `/Invoice/cbc:IssueTime` = `10:31:00`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: The invoice bills the loaded kilometres of the delivery to the store, but according to the receipt advice 17 the truck delivered at 10:40 on the same morning, after this invoice. According to 15 the truck should have arrived on 2026-04-29 at 14:00, which would make the invoice timing natural; the contradiction between 15 and 17 (see 15/F2) decides whether this invoice precedes the service it bills.
- Condition: the transport invoice is issued after the delivery it bills.
- Options: (a, preferred) follows from resolving 15/F2: if delivery is on 2026-04-29, nothing to change; if on 2026-04-30 10:40, issue the invoice after that.
- Needs decision: yes (depends on the delivery day)

### retail/16#F2 · Low · References: the waybill without a type, and no reference to the transport booking
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `BF-WB-26-0231`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-BF-FW-2026`
- Why: The additional document reference resolves to the consignment note 13 but does not say it is a waybill (no DocumentTypeCode/DocumentType). The service was ordered with the transport execution plan request `LD-TR-26-0227` under the framework contract `LD-BF-FW-2026`; the invoice cites neither, so Lumeway cannot match it to its booking except through the consignment ID.
- Condition: the waybill reference states its type, and the invoice identifies the order (transport request) or contract under which the transport was bought.
- Options: (a, preferred) DocumentType "Consignment note" on the reference, plus OrderReference `LD-TR-26-0227` (or ContractDocumentReference `LD-BF-FW-2026`); (b) at least the type on the waybill reference.
- Needs decision: no

## Checked and consistent
- InvoicedQuantity 38 KMT × 2.85 XBL/km = 108.30 XBL = line amount; unit `KMT` agrees with "price per kilometre driven loaded".
- Consignment `LD-CS-26-0228` and carrier Bayforth agree with 11–15; AdditionalDocumentReference `BF-WB-26-0231` resolves to 13.
- Seller/supplier Bayforth and customer Lumeway agree with 11 (transport user and bill-to party Lumeway).

## Outside this review
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`: whether 38 km is the road distance from Marrowdale (Upland State) to the Lumeport old town (Coastal State) on the world's map is a question for the map and route checks.
