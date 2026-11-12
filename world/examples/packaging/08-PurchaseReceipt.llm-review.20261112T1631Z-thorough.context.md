# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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

### packaging/08#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/08#F2 · Low · Customer's bank account on a cash receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `10`
- Why: The purchase is paid in cash (`PaidCashAmount` 70.00, change 11.55); nothing is paid from or to the customer's current account, so its number, branch and bank address have no purpose on the receipt (section 4.8: "a bank account of a party that pays or receives nothing under this document"). The account is Robin Ashdale's master data, used where it belongs in the utilities flow (`utilities/09-Invoice.xml`).
- Condition: the receipt carries no customer bank account, or a payment means that uses it.
- Options: (a) preferred: leave the account out; the customer can still be named on the receipt if the story needs it.
- Needs decision: no

### packaging/08#F3 · Low · Item description carries a tax statement
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description` = `Men's cotton shirt; the state sales tax is added at the till.`
- Why: `Item/Description` is "Text describing this item". The second half describes how the sale is taxed, not the shirt; it belongs to the receipt (a `Note`) or follows from the structured values already there (`Price/PriceAmount` 29.95 net, `TaxInclusivePriceAmount` 31.9, `TaxTotal`). The same text is in 3 examples (`grep -rl --include='*.xml' 'sales tax is added at the till'`).
- Condition: the item description describes only the item; any explanation of the till tax is in a document-level note.
- Options: (a) preferred: drop the tax sentence from the description (the structured tax data say it); (b) move it to `/PurchaseReceipt/cbc:Note`.
- Needs decision: no

### packaging/08#F4 · Low · The store's buying office as contact on a customer's receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- Why: On a receipt the seller's contact is the one a shopper turns to (customer service, returns). Here it is the store's buying office, the contact it uses towards its suppliers (`05-Order.xml`), and the point-of-sale contact's telephone is the buying office's number (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 2511 0411`), so the shop floor is reached through purchasing. Job title and department (`Customer service officer`, `Sales`) fit a receipt, the name and e-mail do not.
- Condition: the supplier's contact and the point-of-sale contact on the receipt are the store's customer-facing contacts, with agreeing name, title, department and numbers.
- Options: (a) preferred: a customer service contact for the store and the shop floor's own telephone for the point of sale.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 × 29.95 = 59.90 = allowance base; 59.90 − 5.00 = 54.90; 6.5 % × 54.90 = 3.5685 → 3.57; 54.90 + 3.57 = 58.47; rounding −0.02 → 58.45 (rounding to 0.05 for cash); 70.00 − 11.55 = 58.45 = PaidAmount; 29.95 × 1.065 = 31.897 → 31.9 TaxInclusivePriceAmount.
- Item identification: `SellersItemIdentification` `BM-778120` is the identifier Brightmarket gave as buyer in `05-Order.xml`; `ManufacturersItemIdentification` `LT-SH-01` is the mill's seller identifier there; `ManufacturerParty` is the mill. Consistent.
- `check_ids.py`: GLN and GTIN pass; IBAN-like account checked by shape.
- Point of sale "Clothing, first floor", cashier, cash register and issue/purchase/transaction time fit a till receipt.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID`, `AdditionalWebSite`, `SocialMediaProfile`: marketing data — refuted for this document because a receipt is the customer-facing document where a store prints its logo, shop and social media.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: legal detail on a receipt — refuted because company details are commonly printed on receipts.
- `/PurchaseReceipt/cbc:TransactionDate`, `cbc:PurchaseDate`, `cbc:IssueDate` all `2026-05-22` 16:05 — refuted because at a till the transaction is begun, completed and receipted in the same minute.
- `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`: company name as a place — refuted because it is the name of the store, which is the place.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`: GTIN with the retailer's company prefix (that of its GLN `9522610900002`) for a shirt made by the mill — refuted for this lens because GS1 lets a retailer number goods made for it under its own brand, and nothing shows `Lumeport` is the mill's brand; prefix 952 is the GS1 prefix reserved for examples, so it is not mistaken for a real number.
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`: a named consumer with residential address on a cash receipt — refuted as a separate finding because a store can issue a named receipt on request (e.g. for exchange or warranty); only the bank account (F2) has no use.
