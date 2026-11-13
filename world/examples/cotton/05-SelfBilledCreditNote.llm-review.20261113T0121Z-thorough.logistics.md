# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/05-SelfBilledCreditNote.xml`, Git blob `ae986b70b136e1ac8647dd8051159b9d408be29a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/05#F1 · Medium · Despatch-advice reference points to the delivery note
- XPath: `/SelfBilledCreditNote/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledCreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` is "a reference to a Despatch Advice associated with this document". `LCF-DN-26-0193` is the farm's Delivery Note (`03-DeliveryNote.xml:/DeliveryNote/cbc:ID`), already cited with the dedicated `DeliveryNoteDocumentReference`. No despatch advice exists in the flow. Same problem as in 04.
- Condition: `DespatchDocumentReference`, if present, refers to a despatch advice; the delivery note is cited only as a delivery note.
- Options: (preferred) drop `DespatchDocumentReference`.
- Needs decision: no

### cotton/05#F2 · Low · Downgrade rests on a classing certificate that says Middling and is dated later
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- XPath: `/SelfBilledCreditNote/cac:AdditionalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/SelfBilledCreditNote/cbc:IssueDate` = `2026-02-14`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- Why: The credit note grants a quality allowance because 2,500 kg were classed Strict Low Middling, and cites `XL-CLS-2026-0042` as the supporting document. Everywhere that certificate is described (02, 07, 08, 10, 11, 15, 16) it says "Grade Middling", it is attached to the lint shipped to the mill as grade Middling, and its signature is dated 2026-02-20, six days after this credit note; the ginning it would class ended only on 2026-02-22 (10). Classing grades lint, not seed cotton, so 2,500 kg of seed cotton can only be downgraded once it has been ginned and its lint classed. The classing report `SCC-CLS-26-0311` cited as work report may be the document meant, but it has only an ID. As it stands the cited certificate contradicts the reason given, and what became of the lower-grade lint is not visible (the 6129 kg shipped are all Middling).
- Condition: the document cited for the downgrade exists at the issue time and states the grade the credit note relies on; the quantity downgraded is stated in the unit and material the classing applied to.
- Options: (preferred) cite only the classing report `SCC-CLS-26-0311` (with a document type) as the basis and drop `XL-CLS-2026-0042`, and word the reason as the lint from 2,500 kg of seed cotton classed SLM; or move the credit note after the classing and give the certificate a remark that covers the SLM part.
- Needs decision: yes (whether the classing found an SLM part, and how that fits the Middling certificate of the shipped lint, is part of the story)

### cotton/05#F3 · Low · Weighbridge ticket cited as a receipt advice
- XPath: `/SelfBilledCreditNote/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `ReceiptDocumentReference` is "a reference to a Receipt Advice associated with this document"; the ID is the gin's weighbridge ticket, cited by 03 as an additional document. No receipt advice is in the flow; the same document is presented as two kinds. Same as in 04.
- Condition: the document is cited as the same kind in 03, 04 and 05, and that kind matches the reference element used.
- Options: (preferred) cite it as an additional document with document type "Weighbridge ticket"; or give it a document type that says it is the gin's receipt advice.
- Needs decision: no

### cotton/05#F4 · Low · Invoice period starts before the only delivery
- XPath: `/SelfBilledCreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`
- XPath: `/SelfBilledCreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- Why: The credit note repeats the invoice period of 04 (2026-02-03 to 2026-02-05) for a delivery that the delivery note and the credit note's own `Delivery` date to 2026-02-05 only.
- Condition: the period and the delivery dates of 03, 04 and 05 describe the same deliveries.
- Options: (preferred) align with the fix of 04: either a delivery period in 03 or a period starting 2026-02-05.
- Needs decision: no

## Checked and consistent
- 2500 KGM × 0.03 = 75.000 XLC; 2500 kg is part of the 18000 kg billed in `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity`.
- `SelfBilledInvoiceDocumentReference` `SCG-SBI-26-0194` with issue date 2026-02-07 resolves to 04; the credit note's payable amount 69.250 XLC is set off in `06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount`.
- Due date 2026-02-16 is the date of the remittance advice 06.
- Item `LCF-SC`, HS 520100 and CPC 01921 agree with 01, 03 and 04.

## Considered and refuted
- `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:ResponseCode` = `2`: "below specification goods" for a grade below the contracted one was checked — consistent, the code fits the reason.
