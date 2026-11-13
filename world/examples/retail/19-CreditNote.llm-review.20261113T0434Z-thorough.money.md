# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### retail/19#F1 · Medium · Credit note names the factor as payee, while its terms settle the credit with the seller
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `494.00`
- Why: `PayeeParty` is "the Party who receives the Payment". The 494.00 of a credit note is owed by the seller to the buyer, so the party that receives a payment under it, if anyone, is Brightmarket (on a refund), and no one when it is set off. Naming the factor as payee says that Harbourline receives 494.00, the opposite direction. The factor matters to the credit for another reason: the invoice was assigned to it (`18-Invoice.xml:/Invoice/cbc:InvoiceTypeCode` = `393`; `18-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`), so Brightmarket pays the invoice to Harbourline, and the payment terms' "next payment to the seller", against which the credit is to be set off, is in fact a payment to the factor. The note and the payee thus describe two different settlements, and neither says whether Brightmarket may deduct 494.00 from the 11856.00 it owes Harbourline.
- Condition: The credit note states one way of settling the credit that fits the factoring: who is to deduct or refund the 494.00, against which payment, and the payee, if present, is a party that receives money under the credit note.
- Options: (a) preferred: remove `PayeeParty` and say in the payment terms that the credit is deducted from the payment of LD-INV-26-0236 to Harbourline Factoring, because that is the usual handling of a credit on a factored invoice (own knowledge of factoring practice); (b) keep the factor as a party that must be informed, but in a role that does not mean receiving payment (e.g. a note), and state who refunds.
- Needs decision: yes

### retail/19#F2 · Low · Payment purpose on a credit line that is settled by set-off
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:PaymentPurposeCode` = `GDDS`
- Why: `PaymentPurposeCode` is "a code signifying the business purpose for this payment" (ISO 20022 purpose, here GDDS "PurchaseSaleOfGoods"). The credit note has no payment means, and its terms settle the credit by deducting it from the next payment; there is no payment for which a purpose would be given, and the invoice it corrects carries no purpose code either. Under the no-filler rule the value has no reason here.
- Condition: The credit note line carries a payment purpose only if a payment (a refund) is made under it.
- Options: (a) preferred: remove it; (b) keep it together with a refund by credit transfer, if F1 is resolved with a refund.
- Needs decision: no

## Checked and consistent
- Line: 1 × 520 = 520.00, at the invoice's price (`18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `520`); the invoice's 5 % promotion support is credited in proportion: 5 % of 520.00 = 26.00; 520.00 − 26.00 = 494.00 tax-exclusive and payable; taxable amount 494.00, tax 0.00.
- The credit equals the invoice's net price of the rejected bench: 11856.00 / 24 = 494.00.
- Tax E, RESALE, STT, supply type GOODS, as on the invoice line.
- The credit corresponds to the receipt advice's rejection (`17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`) and requested action (`17-ReceiptAdvice.xml:/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`), with transport damage as reason; under DDP the seller bears the transport risk, so the seller crediting is consistent.
- Buyer's accounting code 6120 as in the order and invoice.
