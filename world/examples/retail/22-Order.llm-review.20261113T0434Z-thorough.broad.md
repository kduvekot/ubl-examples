# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit bb7d002 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/22#F1 · Medium · Language codes in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/22#F2 · Low · Full card number and security code in the order
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `9902382000715526`
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:CV2ID` = `731`
- Why: the order carries the complete card number and the card verification value. Card industry practice forbids storing or forwarding the verification value after authorisation, and masks the card number in documents (own knowledge of PCI DSS); the purchase receipt of the same customer masks it (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`). The note asks the customer to bring the card at collection, so the order does not need the security code. (The number passes the Luhn check and starts with 99, a range not used by a real card scheme.)
- Condition: the order carries no card verification value, and the card number only as far as the order needs it (masked or tokenised).
- Options: (a, preferred) drop `CV2ID` and mask the number like 21; (b) keep the card account only with holder, network and masked number.
- Needs decision: no

### retail/22#F3 · Low · Ready from Tuesday, but delivery requested from Monday
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- XPath: `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-01`
- Why: the order is placed on Saturday 2026-05-30; the next Tuesday is 2026-06-02. The requested collection period starts on Monday 2026-06-01, the day before the set is said to be ready. The note also reads as the store's message, while the order is the customer's document.
- Condition: the requested period does not start before the day the goods are ready, and the note is a statement the buyer can make.
- Options: (a, preferred) requested period from 2026-06-02; (b) a note in the buyer's voice ("I will collect from Tuesday").
- Needs decision: no

### retail/22#F4 · Low · Retailer's buying office and the customer's bank account in a consumer order
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: as the seller to a consumer, Brightmarket's contact should be its customer service, not the buying office (whose job title and department also contradict its name). The customer pays by credit card; his current account is not used by the order.
- Condition: the seller's contact fits selling to consumers, and the buyer carries only the data the order uses.
- Options: (a, preferred) Brightmarket's customer service as contact, and no financial account for the buyer.
- Needs decision: no

## Checked and consistent
- Arithmetic: 1 × 899.00 = 899.00; tax 6.5 % × 899.00 = 58.44 (58.435 rounded); payable 957.44.
- Standard rate 6.5 % for a consumer sale, as in 21-PurchaseReceipt.
- The item (`BM-551004`, GTIN `9523710000012`, Brackenmere's `BF-GS-01`) is Brightmarket's own garden bench set as bought from Brackenmere in `furniture/08-Order.xml`; HS 940169 and CPC 38112 (wooden frames) fit it.
- Robin Ashdale and his address are described as in 21-PurchaseReceipt; GLNs, GTIN, account and card number pass their check digits.
- Collection at the store with `EXW` and the garden department as delivery location fits click and collect.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`: suspected an Incoterm in a consumer sale — refuted: Ex Works at the seller's premises states correctly that the buyer collects, and Incoterms may be used outside B2B trade.
