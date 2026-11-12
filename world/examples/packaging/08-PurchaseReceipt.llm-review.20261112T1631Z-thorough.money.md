# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/08-PurchaseReceipt.xml`, Git blob `9ece1e4003ae05ddafa0eb8d78c7dfd4d1e85d0d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/08#F1 · Low · The customer's bank account on a receipt paid in cash
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `10`
- Why: UBL defines `Person/FinancialAccount` as "The financial account associated with this person". The purchase was paid in cash (`PaymentMeansCode` 10, 70.00 given, 11.55 change); nothing in the receipt is paid from or to Robin Ashdale's current account. The account, with branch and full bank address, looks copied from the person's master data, where it serves the direct debits of the utilities flow (`utilities/09-Invoice.xml` pays by direct debit, payment means 49). A retailer has no reason to print a cash customer's bank account on a till receipt. The account occurs in 7 XML files (`grep -rl --include='*.xml' XB64BLUM38010007251840 world/examples`).
- Condition: the receipt carries the customer's financial account only if the purchase uses it (e.g. a payment by debit card or transfer from that account, or a refund to it).
- Options: (a, preferred) remove `cac:FinancialAccount` from the customer's `Person` in this receipt; (b) change the story to a card or account payment that uses it.
- Needs decision: no

## Checked and consistent
- Line: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `2` × `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `29.95` = 59.90 = `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:BaseAmount` = `59.90`; minus the discount `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:Amount` = `5.00` (ChargeIndicator false, reason 95 Discount, "5.00 off the pair" for 2 shirts) = 54.90 = `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:LineExtensionAmount` = `54.90`.
- Tax: 6.5 % × 54.90 = 3.5685 → `/PurchaseReceipt/cac:TaxTotal/cbc:TaxAmount` = `3.57` (XBL has 2 decimals); taxable amount equals the discounted line; category S, scheme STT matches Brightmarket's STT registration in Coastal State; the item text "the state sales tax is added at the till" agrees with a net shelf price.
- Price: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:TaxInclusivePriceAmount` = `31.9` = 29.95 × 1.065 = 31.897 rounded.
- Totals: 54.90 + 3.57 = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `58.47`; `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount` = `-0.02` rounds to the 0.05 step for cash, giving `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableAmount` = `58.45`.
- Payment: `/PurchaseReceipt/cac:Payment/cbc:PaidCashAmount` = `70.00` − `/PurchaseReceipt/cac:Payment/cbc:CashChangeAmount` = `11.55` = `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `58.45` = payable amount (UBL: "Paid Amount = Paid Cash Amount - Cash Change Amount").
- Against the purchase: Brightmarket bought the shirt at 14.50 (`07-Invoice.xml`), exempt for resale; charging STT on the retail sale is consistent with that exemption.

## Considered and refuted
- `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount` = `-0.02`: UBL's definition says the rounding is "added to produce the line extension amount" — refuted as a problem of the example: the definition text is a known slip in UBL (the element rounds the payable amount); the value does exactly that.
