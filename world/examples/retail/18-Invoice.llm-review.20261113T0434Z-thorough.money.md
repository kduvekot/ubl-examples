# LLM review: 18-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/18-Invoice.xml`, Git blob `4c83015ab6e72109b8aa59490284886f5aa405ef` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### retail/18#F1 · Medium · Pricing reference carries no pricing, and a lead time that contradicts the catalogue
- XPath: `/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- Why: `PricingReference` is "a reference to pricing and item location information associated with this invoice line", and its `OriginalItemLocationQuantity` "an original set of location-specific properties (e.g., price and quantity) associated with this item". The only thing it carries is a lead time of 5 days: no original price, no quantity band, no allowance, so as a pricing reference it says nothing about the price billed. The original location-specific properties of this item are those of the catalogue the order is based on, and there the lead time is 3 days (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `3`), so the "original" value given here contradicts the original.
- Condition: The invoice line's pricing reference either is absent or carries the original pricing information of the item (e.g. the catalogue's price 520 per bench with its quantity band), and any lead time it repeats is the catalogue's.
- Options: (a) preferred: remove `PricingReference`, because the billed price equals the catalogue and order price and needs no reference; (b) fill `OriginalItemLocationQuantity` from the catalogue line (price, minimum and maximum quantity, lead time 3 days), if the invoice is meant to show the price basis.
- Needs decision: no

### retail/18#F2 · Low · Invoice bills 24 benches although the receipt advice it refers to accepted 23
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `24`
- XPath: `/Invoice/cac:InvoiceLine/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `BS-RA-26-0235`
- Why: The invoice was issued after the receipt advice (15:52 against 15:21 on the same day, `17-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:21:00`) and refers to it at document and line level, but bills all 24 despatched benches, while the receipt line it cites received 23 and rejected one (`17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`; `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`). The rejected bench is then credited two days later (`19-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `1`), which matches the buyer's requested action (`17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectActionCode` = `CREDIT`). Invoicing on the despatched quantity and crediting afterwards is a common practice, but an invoice that bases itself on a receipt line usually bills the received quantity; and since the invoice is factored, billing an amount the seller already knows is disputed transfers a receivable of 494.00 that is not owed. Whether the story intends invoice-on-despatch is a decision.
- Condition: Either the invoice bills the accepted quantity of the receipt it refers to (23, payable 11362.00) and the credit note is not needed for the bench, or the invoice is based on the despatch only (no receipt reference) and the credit note corrects it.
- Options: (a) preferred: keep 24 and drop the receipt references from the invoice, so it is visibly an invoice on despatch, corrected by the credit note, because that keeps the flow's credit note; (b) bill 23 and let the credit note go, which changes the flow.
- Needs decision: yes

### retail/18#F3 · Low · Tax point date eight days after delivery and invoice, with no event behind it
- XPath: `/Invoice/cac:InvoiceLine/cbc:TaxPointDate` = `2026-05-08`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- Why: The invoice line's `TaxPointDate` is "the date of the Invoice Line, used to indicate the point at which tax becomes applicable". The goods were delivered and received on 2026-04-30 (`17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`; `19-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cac:Delivery/cbc:ActualDeliveryDate` = `2026-04-30`) and the invoice is dated the same day; nothing in the flow happens on 2026-05-08 (the promotion starts on 2026-05-11, payment is due on 2026-05-30). In sales tax practice the tax point is the sale, delivery or invoice (own knowledge). The tax is exempt here, so the date has no effect on the amount, but it has no business reason as given.
- Condition: The tax point date is the date of an event that fixes the tax point in this world (delivery or invoice, 2026-04-30), or it is absent.
- Options: (a) preferred: 2026-04-30, the date of delivery and invoice; (b) remove it, as an exempt sale with invoice date equal to delivery date needs no separate tax point.
- Needs decision: yes

### retail/18#F4 · Low · Line payment terms repeat the document's terms
- XPath: `/Invoice/cac:InvoiceLine/cac:PaymentTerms/cbc:Note` = `The promotion stock is paid with the invoice, 30 days net.`
- Why: Line-level `PaymentTerms` is "a specification of payment terms associated with this invoice line", needed where a line is paid differently from the rest. The invoice has one line, and the document's terms already say 30 days net with the due date 2026-05-30 (`/Invoice/cbc:DueDate` = `2026-05-30`). The note adds nothing ("paid with the invoice" is what any invoice line is); under the no-filler rule it has no reason.
- Condition: The line has no payment terms, or terms that differ from the document's.
- Options: (a) preferred: remove the line's `PaymentTerms`.
- Needs decision: no

## Checked and consistent
- Line: 24 × 520 = 12480.00; allowance 5 % of 12480.00 = 624.00; tax-exclusive 11856.00; taxable amount 11856.00 (net of the allowance); tax 0.00; payable 11856.00, the same as the order's anticipated total (`08-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11856.00`).
- Penalty: 1.5 % of 11856.00 = 177.84 (`/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `177.84`), from 2026-05-31, the day after the due date 2026-05-30 (30 days net from 2026-04-30, as in the catalogue).
- Factoring: invoice type 393 "Factored invoice" (`/Invoice/cbc:InvoiceTypeCode` = `393`), payee Harbourline Factoring and payee account in the name Harbourline Factoring Ltd; account XB51BLUM38020502304038 and the RF reference RF42LDINV260236 pass `check_ids.py`.
- Tax: E, RESALE, STT on the line, the allowance and the subtotal, as in the catalogue and order; supply type GOODS.
- Price 520 is the catalogue's trade price, within its validity.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode` = `6120`: suspected a copy of a party's master data — refuted, it is the buyer's own code from its order (`08-Order.xml:/Order/cbc:AccountingCostCode` = `6120`), which the invoice is expected to repeat.
