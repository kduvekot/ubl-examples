# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
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

### retail/22#F1 · Medium · The order carries the full card number and the card security code
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `9902382000715526`
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:CV2ID` = `731`
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- Why: `PaymentMeans` in an order is the "expected means of payment". For a click-and-collect order the shop needs to know which card will pay, and, if the card is charged online, the card scheme authorises it at checkout; the order document itself does not need the unmasked number, and the card verification value must never be stored or passed on after authorisation (PCI DSS, own knowledge). The note even tells the customer to bring the card to the store, so the card is identified again at collection. An example that puts the full PAN and the CV2 into a business document shows a practice no card scheme allows. The purchase receipt of the same flow shows the card masked (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`). `CV2ID` occurs in this example only (counted with `grep -rl --include='*.xml' CV2ID world/examples/`).
- Condition: The order identifies the card without its security code and without the full card number (e.g. masked PAN, network, holder, expiry), or carries no card data at all.
- Options: (a) preferred: masked PAN and no `CV2ID`, because that is how an order system holds a card after authorisation; (b) no card account, only the payment means code, since payment happens at collection.
- Needs decision: no

### retail/22#F2 · Low · The buyer's bank account is carried on an order paid by credit card
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`
- Why: The order is to be paid by credit card (`/Order/cac:PaymentMeans/cac:CardAccount/cbc:CardTypeCode` = `CREDIT`); nothing is paid from or to the buyer's current account under it, and a shop does not need a consumer's account number to sell click-and-collect. The account (with its branch and bank) looks copied from the buyer's master data; it appears the same way on the earlier purchase receipt (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`), which was paid by debit card.
- Condition: The order carries the buyer's financial account only if a payment or refund under the order uses it.
- Options: (a) preferred: remove the person's financial account.
- Needs decision: no

## Checked and consistent
- Line: 1 SET × 899 = 899.00; tax 899.00 × 6.5 % = 58.435 → 58.44 (S, STT); payable 899.00 + 58.44 = 957.44 (`/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `957.44`).
- The rate 6.5 % is the one of the purchase receipt (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `6.5`); a consumer sale is taxable, unlike the trade sales for resale.
- Card: payment means 54 "Credit card" matches card type CREDIT; validity 2025-03-01 to 2029-02-28 covers the order date; the PAN passes the Luhn check (calculated) and starts with 9, the major industry identifier for national assignment, so it cannot be a real scheme's card (own knowledge of ISO/IEC 7812).
- The order is placed 2026-05-30, after the promotion (to 2026-05-24); the bench set is not a promoted item, so no promotional price applies.
