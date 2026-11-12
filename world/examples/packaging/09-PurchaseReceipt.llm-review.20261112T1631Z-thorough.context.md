# LLM review: 09-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/09-PurchaseReceipt.xml`, Git blob `8c680565e9cab9b2d106e8f8d8cf3831c5abddd0` (committed)
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

### packaging/09#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/09#F2 · Low · Three shirts without the pair discount given the day before
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `3`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:LineExtensionAmount` = `35.940`
- XPath: `08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Two shirts: 5.00 off the pair`
- Why: On 2026-05-22 the same store, till and cashier gave 5.00 off a pair of the same shirt (`08-PurchaseReceipt.xml`). On 2026-05-23 three shirts, which contain a pair, are sold at the full price (3 × 11.98 XLC = 35.94 XLC = 3 × 29.95 XBL at 0.4). Either the promotion ended in between, which neither receipt says, or the discount is missing here.
- Condition: the two receipts agree on the promotion: either this line carries the pair discount (converted to coral), or one of the receipts states when the offer applies.
- Options: (a) state the offer's validity (e.g. a one-day offer) on the receipt of 22 May; (b) apply 5.00 XBL (2.00 XLC) off the pair here and correct the totals and tax. Preference for (a) if the story is a one-day offer, since it keeps this receipt's arithmetic.
- Needs decision: yes

### packaging/09#F3 · Low · Item description carries a tax statement
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description` = `Men's cotton shirt; the state sales tax is added at the till.`
- Why: `Item/Description` is "Text describing this item"; the second half describes the taxation of the sale, which the structured `TaxTotal` already gives. Same text in 3 examples (`grep -rl --include='*.xml' 'sales tax is added at the till'`).
- Condition: the item description describes only the item.
- Options: (a) preferred: drop the tax sentence; (b) move it to `/PurchaseReceipt/cbc:Note`.
- Needs decision: no

### packaging/09#F4 · Low · Contacts do not fit the receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The store's contact on a customer receipt is its buying office (`buying@brightmarket.example`), and the point of sale is reached on the buying office's number; a shopper needs the store's customer service. The customer's contact is "Purchasing" in Sales as customer service officer, so name and department contradict each other. 89 examples have a `Purchasing` or `Buying office` contact in Sales (XPath count over `world/examples/*/*.xml`).
- Condition: the store's contacts on the receipt are customer-facing, and the customer's contact has agreeing name, title and department.
- Options: (a) preferred: store customer service contact and the shop floor's own number; a purchasing title and department for Velumi's contact, or no customer contact at all, since a till purchase does not need one.
- Needs decision: no

## Checked and consistent
- Currency conversion: pricing XBL → XLC at 0.4 (29.95 × 0.4 = 11.98); tax currency XLC → XBL at 2.5 (35.94 × 2.5 = 89.85 = 3 × 29.95); 6.5 % of 35.940 = 2.3361 → 2.336 XLC and of 89.85 = 5.840 → 5.84 XBL; totals 35.940 + 2.336 = 38.276 = PaidAmount. The two rates are reciprocal, and the note "Paid in coral: the card's currency was chosen at the till." agrees with `DocumentCurrencyCode` XLC and the card payment.
- Card: `PaymentMeansCode` 54 (credit card), `CardTypeCode` CREDIT and holder `VELUMI TRADING` agree with the customer.
- Store, till C1, cashier and point of sale agree with `08-PurchaseReceipt.xml`.

## Considered and refuted
- `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`: a credit card in "A receipt for a purchase made with cash or cash equivalents" — refuted because card payment at a till counts as a cash equivalent for a point-of-sale receipt.
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Lisavan street tagged `en-XB` — refuted because the English tag follows the sender's country in all examples (the Bayvarran store writes English as used in Bayvarra).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649`: a wholesaler of household goods buying three shirts at retail — refuted because a company buying a few items for its own use with a company card is plausible.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:SocialMediaProfile`: marketing data — refuted for a receipt, the customer-facing document.
