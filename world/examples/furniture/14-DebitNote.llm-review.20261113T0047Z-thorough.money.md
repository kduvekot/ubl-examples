# LLM review: 14-DebitNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/14-DebitNote.xml`, Git blob `46010db5dff2abd14661e7fabad9e7fd90e953c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/14#F1 · Medium · The payee is the accounting customer; the accounting supplier is not the seller of the debited service
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Brightmarket Stores Corp`
- Why: The store issues this debit note (`/DebitNote/cbc:ID` = `BS-DOC-26-0580`) to charge the maker 85.00 for return transport; the money flows from the maker to the store. The store is the seller of the debited service (`SellerSupplierParty`, and the item ID `BM-SVC-RT` is the store's) and the payee, but the accounting roles are kept as in the original sale: the maker is `AccountingSupplierParty`, the store `AccountingCustomerParty`. In UBL's billing documents the accounting supplier is the party that claims the amount and the accounting customer the party that settles it; here the payee (`PayeeParty`, "The Party who receives the Payment") is the accounting customer, so the document says the debtor receives the payment. Either the accounting roles or the seller/buyer roles contradict the direction of the money. The same pattern (PayeeParty equal to AccountingCustomerParty, seller/buyer reversed against the accounting parties) occurs in sea/28-DebitNote; the third debit note, tender/34-DebitNote, has no PayeeParty (checked by script over the three `*DebitNote*.xml`).
- Condition: The accounting supplier of the debit note is the party that claims the 85.00 and receives the payment, and the accounting customer is the party that pays it, consistently with the seller and buyer of the debited service; `PayeeParty` is present only if the payee differs from the accounting supplier.
- Options: (preferred) make the store the accounting supplier and the maker the accounting customer, and drop `PayeeParty` (it would equal the accounting supplier); or, if the world means a "buyer-issued debit note" that keeps the original roles, record that reading as a decision and a finding for the UBL TC write-up, since UBL does not define it.
- Needs decision: yes

### furniture/14#F2 · Low · Payment note calls the debit note an invoice
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BS-DOC-26-0580`
- Why: `PaymentNote` is "Free-form text applying to the Payment for the owner of this account". The document is a debit note (`/DebitNote/cbc:DebitNoteTypeCode` = `383`), not an invoice.
- Condition: The payment note names the document as a debit note.
- Options: (preferred) "Debit note BS-DOC-26-0580".
- Needs decision: no

### furniture/14#F3 · Low · The credit note's restocking deduction repeated on the transport line
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cbc:Amount` = `3477.00`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Restocking deduction`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- Why: `BillingReferenceLine/AllowanceCharge` is "An allowance or charge applicable to the transaction line". The debit note bills return transport (85.00); the referenced credit note line's amount and its restocking deduction play no part in that charge. The values agree with `13-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `3477.00`, but repeating the deduction here reads as if it were relevant to the debit, which it is not; it looks copied from the credit note (section 4.8). If the store meant to dispute the deduction, the document does not say so. The deduction itself is questioned in 13-CreditNote's review (return requested by the maker, `/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`).
- Condition: The billing reference line carries only what the transport debit needs (the referenced credit note line), or the document says what the store does about the deduction.
- Options: (preferred) keep the reference to credit note line 1 and drop the amount and the allowance; or, if the store disputes the deduction, state it (e.g. a discrepancy response) and keep the figures as evidence.
- Needs decision: no

## Checked and consistent
- Line: 1 × 85 per `/DebitNote/cac:DebitNoteLine/cac:Price/cbc:BaseQuantity` = `1` service unit = `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `85.00` = `/DebitNote/cac:DebitNoteLine/cbc:TaxInclusiveLineExtensionAmount` = `85.00` (tax 0.00) = `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `85.00`; taxable amount 85.00.
- Tax: exempt STT with reason `SVCB2B` "Service to a business" for a transport service between two businesses, the same exempt reason the world uses for B2B services in other flows (e.g. sea/18-Invoice, air/10-Invoice).
- Due date: 2026-05-04 + 30 days = 2026-06-03 = `/DebitNote/cbc:DueDate` = `2026-06-03`, as "30 days net" says.
- Payment: `/DebitNote/cac:PaymentMeans/cbc:PaymentID` = `RF86BSDOC260580` passes the ISO 11649 check and is built from the store's own number (the store receives the money); the account `XB48BLUM38010001570935` passes the IBAN-style check and is the store's account in `13-CreditNote.xml:/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB48BLUM38010001570935`.
- Payment purpose `SCVE` (PurchaseSaleOfServices) fits a transport service.
- Return date `/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02` lies within the requested return period of 12-InstructionForReturns (2026-04-29 to 2026-05-02) and before the credit note (2026-05-03).

## Considered and refuted
- `/DebitNote/cac:LegalMonetaryTotal`: suspected incomplete totals (no tax-exclusive or tax-inclusive amount, which 09-Invoice and 13-CreditNote carry). Refuted because both are optional, no tax is due and the line carries its tax-inclusive amount; the payable amount is unambiguous.
- `/DebitNote/cac:DebitNoteLine/cbc:PaymentPurposeCode` = `SCVE`: suspected an element meant for the payment itself placed on a line. Refuted because UBL 2.5 defines it on the debit note line ("A code signifying the business purpose for this payment"), and the line is the service being paid for.
