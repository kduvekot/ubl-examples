# LLM review: 14-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/14-Invoice.xml`, Git blob `1173f55bda6f9ffdefd8413a5ce62500697f236a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### road/14#F1 · High · Freight invoice refers to a receipt advice issued the next day
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-25`
- XPath: `/Invoice/cbc:IssueTime` = `11:07:00`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `LD-RA-26-0164`
- Why: The invoice, issued on 2026-03-25 at 11:07, points to line 1 of receipt advice LD-RA-26-0164. That receipt advice is the revised one, issued on 2026-03-26 at 10:48 (`13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueDate` = `2026-03-26`). Even the first receipt advice (`11-ReceiptAdvice.xml`, LD-RA-26-0162) is issued only at 15:40 on 2026-03-25, after the invoice. The carrier cannot cite a document of the consignee that does not yet exist; the referenced line is also the buyer's receipt line, not something the carrier holds.
- Condition: every document the invoice references exists at the invoice's issue date and time.
- Options: (a) preferred: base the carrier's proof of delivery on its own documents, i.e. the signed waybill already referenced and the actual delivery event (09:40), and remove the receipt line reference; (b) issue the freight invoice after 2026-03-26 10:48 if it must cite the corrected receipt advice.
- Needs decision: no

### road/14#F2 · Low · Goods item linked to the bench line only, for freight on the whole load
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cbc:LineID` = `1`
- Why: The invoice charges a full truck load per kilometre (`/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Full truck load, price per kilometre driven loaded, tolls included.`), i.e. the whole consignment LD-CS-26-0152 of 25 pallets. Its one goods item refers only to receipt line 1 (the benches); the side frames on line 2 of the same receipt advice are not covered, so the invoiced delivery looks partial.
- Condition: the delivery the freight invoice describes covers the whole consignment (or carries no goods item at all, since the consignment ID identifies it).
- Options: (a) preferred: remove the GoodsItem (see F1) and keep the consignment; (b) add a second goods item for line 2.
- Needs decision: no

### road/14#F3 · Low · Waybill referenced without its document type
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TH-WB-26-0159`
- Why: An invoice's AdditionalDocumentReference can be any supporting document; this one has only an ID. Nothing in the invoice says it is the CMR waybill (`08-Waybill.xml`), which is the carrier's proof of the transport invoiced.
- Condition: the reference states its document type (waybill / CMR).
- Options: (a) preferred: add DocumentTypeCode for the waybill; (b) add a DocumentDescription.
- Needs decision: no

## Checked and consistent
- Actual delivery 2026-03-25 09:40 equals `11-ReceiptAdvice.xml` and `13-ReceiptAdvice.xml`; the invoice is issued after it.
- Physics: 186 km loaded for Ferrano–Marrowdale with a border crossing fits the transit of 2026-03-23 16:20 to 2026-03-25 09:40 with overnight stops; the 61 l of diesel in the waybill give 32.8 l/100 km, plausible for a loaded truck with trailer.
- Consignment LD-CS-26-0152 and carrier Trasvia Haulage agree with the waybill; the freight is billed to the consignee, as the waybill's collect payment terms say.
