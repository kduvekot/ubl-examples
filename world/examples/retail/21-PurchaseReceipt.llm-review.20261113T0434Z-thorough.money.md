# LLM review: 21-PurchaseReceipt.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/21-PurchaseReceipt.xml`, Git blob `7f75d1791cf92b3eb6f0f963657d0181e309ff88` (committed)
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

### retail/21#F1 · Low · Payment and transaction identifiers carry another date than the payment
- XPath: `/PurchaseReceipt/cac:Payment/cbc:ID` = `BM-G2-26-0518-0047`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:TransactionID` = `TX-26-0518-773104`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:PaidDate` = `2026-05-15`
- Why: Both identifiers are built from the register (G2), the year and a month-day part, 0518, i.e. 18 May 2026, a Monday; the payment was made at the till on Friday 15 May 2026 at 11:42, the same moment as the purchase (`/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`). The sales document reference has the same 0518 (`/PurchaseReceipt/cac:SalesDocumentReference/cbc:ID` = `BM-DEL-26-0518-07`). An identifier that encodes a date reads as a statement of that date; here it contradicts the payment date. (The 0518 also matches neither the booked delivery "Saturday", 16 May, nor the requested delivery date.)
- Condition: Identifiers of the payment that encode a date encode the payment date (2026-05-15), or encode no date.
- Options: (a) preferred: 0515 in both identifiers (and in the sales document reference, if it is the sale of the same day), because the receipt otherwise reads as recorded on another day; (b) identifiers without a date part.
- Needs decision: no

### retail/21#F2 · Low · The customer's bank account is carried on a receipt paid by debit card
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `55`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`
- Why: The payment is a debit card payment at the till, identified on the receipt, as is usual, by the masked card number and the issuer. The full account number of the customer, with its branch and bank address, plays no part in it: nothing is paid to or collected from that account under this receipt, and a till does not learn the account behind a card (own knowledge of card payments). It looks copied from the customer's master data into a document that does not use it. The same account appears in the consumer's later order, which is also paid by card (`22-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`).
- Condition: The receipt carries the customer's financial account only if the purchase is paid from or refunded to it by transfer.
- Options: (a) preferred: remove the person's financial account, as the card account already identifies the payment; (b) keep it with a reason in the story, e.g. a refund by transfer promised on the receipt.
- Needs decision: no

## Checked and consistent
- Price: regular 749.00, promotion 10 % = 74.90, promotional price 674.10 (`/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `674.1`), within the promotion period 2026-05-11 to 2026-05-24 of the retail event.
- Tax: 674.10 × 6.5 % = 43.8165 → 43.82 on the line; tax-inclusive line 717.92, equal to the tax-inclusive price; delivery charge 25.00 also at 6.5 % (S, STT); taxable 699.10 × 6.5 % = 45.4415 → 45.44; totals 674.10 + 25.00 = 699.10, 699.10 + 45.44 = 744.54 payable and paid (`/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `744.54`).
- The rate 6.5 % of the state sales tax is the same as in the consumer's order (`22-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `6.5`); the item's description says the tax is added at the till, matching a tax-exclusive price with tax added.
- Card: debit card (55, DEBIT), issued by the customer's bank BLUMXBLX, PAN masked; payment status approved.

