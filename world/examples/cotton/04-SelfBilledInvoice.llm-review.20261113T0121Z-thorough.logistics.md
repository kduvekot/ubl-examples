# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/04-SelfBilledInvoice.xml`, Git blob `7ff28661ff5e42f702b07e4477e9454c7a6c7ebb` (committed)
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

### cotton/04#F1 · Medium · Despatch-advice reference points to the delivery note
- XPath: `/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` is "a reference to a Despatch Advice associated with this document". `LCF-DN-26-0193` is the farm's Delivery Note (`03-DeliveryNote.xml:/DeliveryNote/cbc:ID`), which the invoice already cites with the dedicated `DeliveryNoteDocumentReference` and in the line's `DeliveryNoteLineReference`. No despatch advice exists in the flow; the same ID in the despatch-advice reference presents the delivery note as a document of another kind.
- Condition: `DespatchDocumentReference`, if present, refers to a despatch advice; the delivery note is cited only as a delivery note.
- Options: (preferred) drop `DespatchDocumentReference`; or add a despatch advice to the flow if the farm really sends one (changes the story).
- Needs decision: no

### cotton/04#F2 · Low · Invoice period starts before the only delivery
- XPath: `/SelfBilledInvoice/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`
- XPath: `/SelfBilledInvoice/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- Why: The invoice bills one delivery note with one actual delivery date, 2026-02-05, and its own `Delivery` gives the same date. The invoice period from 2026-02-03 implies deliveries over three days (three trailer loads, per 03's note), which neither the delivery note nor the invoice records. The same period is in 05 (`05-SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:InvoicePeriod/cbc:StartDate`).
- Condition: the invoice period and the delivery date(s) of the invoice and of 03 describe the same deliveries.
- Options: (preferred) if the three loads came on 2026-02-03 to 2026-02-05, give the delivery note a delivery period (or one delivery per load) and the invoice the matching dates; otherwise start the period on 2026-02-05.
- Needs decision: no

### cotton/04#F3 · Low · Ginning outturn report cited before the ginning was done
- XPath: `/SelfBilledInvoice/cac:WorkReportDocumentReference/cbc:ID` = `SCG-OUT-26-0311`
- XPath: `/SelfBilledInvoice/cbc:IssueDate` = `2026-02-07`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:StartDate` = `2026-02-07`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- Why: `WorkReportDocumentReference` is "a reference to a Work Report associated with this document". The ID reads as the gin's outturn report (`OUT`), i.e. the report of what the ginning yielded. The goods certificate 10 states that ginning ran from 2026-02-07 to 2026-02-22, so on the invoice's issue day (2026-02-07, 15:50) the ginning had just begun and no outturn could be reported. The invoice is priced per kilogram of seed cotton delivered (18000 kg × 0.226), not on outturn, so the invoice does not need the report either. The reference carries only an ID and no type.
- Condition: every work report the invoice cites exists at its issue time and is something the invoice is based on, and says what kind of report it is.
- Options: (preferred) drop the reference, or replace it with the report the invoice really rests on (the weighbridge ticket is already cited); or move the invoice after the outturn if the price depends on it (changes the story).
- Needs decision: no

### cotton/04#F4 · Low · Weighbridge ticket cited as a receipt advice
- XPath: `/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `ReceiptDocumentReference` is "a reference to a Receipt Advice associated with this document". The ID is the gin's weighbridge ticket (03: "weighed at the gin"; prefix `WB`), cited in 03 as an additional document. A weighbridge ticket records a weighing; whether it is the gin's receipt advice is not said anywhere, and no receipt advice is in the flow. A reader of 03 and 04 sees the same document as two different kinds.
- Condition: the document is cited as the same kind in 03, 04 and 05, and that kind matches the reference element used.
- Options: (preferred) cite it as an additional document with document type "Weighbridge ticket" in 03, 04 and 05; or, if the gin's weighbridge ticket is meant as its receipt advice, say so with a document type and keep `ReceiptDocumentReference`.
- Needs decision: no

### cotton/04#F5 · Low · DAP without a named place, and a haulage charge to the buyer
- XPath: `/SelfBilledInvoice/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `CAB`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true`
- Why: An Incoterms rule is always used with a named place (Incoterms 2020, own knowledge); `DeliveryTerms` has no `DeliveryLocation`, and only the separate `Delivery` names the gin's weighbridge. Under DAP the seller (the farm) bears the cost of carriage to the named place; the invoice nevertheless adds a cartage charge (`CAB`, "Haulage allowance", 180.000 XLC) that the buyer pays. The two statements about who pays for the haulage contradict each other unless the season agreement deviates from DAP, which nothing says.
- Condition: the delivery terms name their place, and who pays for the haulage to the gin is stated once, consistently by the terms and the charge.
- Options: (preferred) add the gin as the named place of DAP and explain the haulage payment as an agreed allowance outside the Incoterms rule (or make it a price component); or use a rule under which the buyer pays carriage (e.g. FCA at the farm) if the gin really pays for the haulage.
- Needs decision: yes (who bears the haulage is part of the season agreement)

## Checked and consistent
- 18000 KGM × 0.226 = 4068.000 XLC; per-unit haulage 0.010 × 18000 kg = 180.000 XLC; quantity equals `03-DeliveryNote.xml:/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity`.
- `SelfBilledInvoiceDocumentReference` `SCG-SBI-26-0191` with issue date 2026-01-13 resolves to 01, and the prepaid 1017.000 XLC on 2026-01-13 matches 01.
- `DeliveryNoteLineReference` (line 1 of `LCF-DN-26-0193`) resolves to the only line of 03.
- Payment terms "45 days net" from 2026-02-07 give 2026-03-24 (21 days to 28 February + 24), as stated in all three due dates.
- `OrderReference` `SCG-SEASON-2026/03` is the same call-off as in 03 and 05.

## Considered and refuted
- `/SelfBilledInvoice/cac:PurchaseReference/cbc:ID` = `LCF-FIELD-07`: a field number in a purchase reference was suspected as misuse — refuted because `PurchaseReference` is "a reference to an object … to which this Invoice relates", and the field the cotton was grown on is such an object.
- `/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID` = `SCG-SEASON-2026`: no target in the flow — refuted because the season agreement is not a UBL document, and the element names what it is.
