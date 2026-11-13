# LLM review: 06-OrderResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/06-OrderResponse.xml`, Git blob `8c32d38abff802a363b6a976f771dad7ef600e7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/06#F1 · High · Confirmed payable amount and balance differ from what the invoice for the same order bills
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`
- XPath: `/OrderResponse/cbc:Note` = `Accepted. A deposit of 10,000.00 lume is due on acceptance; the balance 45 days after shipment.`
- Why: the order response accepts the order (`OrderResponseCode` AP) with a `LegalMonetaryTotal` whose `PayableAmount` is "the amount of the monetary total to be paid": 50,688.00 lume, so the balance after the 10,000.00 deposit is 40,688.00. The invoice for this order bills 53,778.00 (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`), adding sea freight and cargo insurance (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`), and asks a balance of 43,778.00 (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`). The deposit share shifts accordingly: 10,000 / 50,688 = 19.73 % here against `22-Invoice.xml:/Invoice/cac:PaymentTerms[1]/cbc:PaymentPercent` = `18.59` there. The seller's response is the place where charges not anticipated in the order would be announced; it confirms the order "as ordered" with no charge, under CIF delivery terms (`/OrderResponse/cac:DeliveryTerms/cbc:ID` = `CIF`), so the two documents state different amounts to be paid for the same sale.
- Condition: the amount the order response confirms as payable (and the balance its note implies) equals what the invoice for the order bills, or the order response states the charges that will be added and the invoice adds only those.
- Options: (a) preferred: announce the CIF freight and insurance in the order response (document-level charges with their amounts or an estimate, totals including them), so that order response and invoice agree; (b) treat 520 lume as the CIF price and remove the separate freight and insurance charges from the invoice; (c) if the charges are deliberately billed only later, say so in the response's note. The choice decides how CIF is priced in the flow.
- Needs decision: yes

### sea/06#F2 · Low · Payment note calls the sales order number an invoice
- XPath: `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123`
- XPath: `/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: `PaymentNote` is "free-form text applying to the Payment for the owner of this account". The payment it applies to is the deposit due on acceptance (`/OrderResponse/cac:PaymentTerms/cbc:ID` = `DEPOSIT`), requested by this order response; no invoice exists at that time, and LD-SO-26-0123 is the seller's sales order number, not an invoice number (the only invoice of the sale is LD-INV-26-0147, `22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147`). The note tells Lumeway's accounts department to expect the deposit against an invoice that does not exist. The structured reference `/OrderResponse/cac:PaymentMeans/cbc:PaymentID` = `RF41LDSO260123` (check digits correct) is built on the same sales order number, which fits.
- Condition: the payment note names the deposit and the document or number it is paid against as what it is (the sales order, or this order response), not as an invoice.
- Options: (a) preferred: "Deposit on sales order LD-SO-26-0123", matching the RF reference; (b) drop the note, since the RF reference already identifies the payment.
- Needs decision: no

## Checked and consistent
- Lines: 96 × 520.00 = 49,920.00 and 12 × 64.00 = 768.00; `TaxInclusiveLineExtensionAmount` equals the line amount and `TotalTaxAmount` is 0.00 on each line at 0 %; sum 50,688.00 = `/OrderResponse/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00` = taxable amount; tax 0.00. Prices and quantities are those of `05-Order.xml`.
- Deposit: `/OrderResponse/cac:PaymentTerms/cbc:Amount` = `10000.00`, due `/OrderResponse/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-09`, the same date as `/OrderResponse/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-09` and as the note's amount; the invoice records it as paid on 2026-05-08 and received on 2026-05-09 (`22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:ReceivedDate` = `2026-05-09`), 10,000.00, deducted as `PrepaidAmount`.
- Balance due date: the note's "45 days after shipment" with shipment on 2026-05-14 gives 2026-06-28, which is the invoice's due date (`22-Invoice.xml:/Invoice/cbc:DueDate` = `2026-06-28`).
- Account: `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB19BLUM38712001466206` passes the IBAN-style check (check_ids.py) and is Lumeway's own account, the same as in `road/17-RemittanceAdvice.xml`; the deposit is paid before the receivable is assigned to Harbourline Factoring, so Lumeway's own account (not the factor's) is right here. Account currency XBL matches the document currency.
- Payment channel RTNS on the Trade Accord rail and charge bearer SHAR are the same as in the invoice's payment means.

## Considered and refuted
- `/OrderResponse/cac:PaymentTerms/cbc:Note` = `Deposit due on acceptance.`: suspected that a due date one day after the response (2026-05-09 against acceptance on 2026-05-08) contradicts "on acceptance" — refuted because a due date of the next banking day is an ordinary reading of "due on acceptance", and the deposit was in fact paid on 2026-05-08.
- `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` = `387120`: suspected a mismatch with the branch of the invoice's account (380205) — refuted because the invoice's account belongs to Harbourline Factoring, a different account holder after the assignment; the two accounts are not meant to be the same.

## Outside this review
- `22-Invoice.xml`: the balance terms' note says "30 days net" while the due date 2026-06-28 is 45 days after the invoice and shipment date of 2026-05-14 (as this order response's note says); this lies in the invoice.
