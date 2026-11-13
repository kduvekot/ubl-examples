# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 44b84c0 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/22#F1 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/22#F2 · Low · Full card number and card verification value in the order
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `9902382000715526`
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:CV2ID` = `731`
- Why: CardAccount is the card "that constitutes this means of payment", and CV2ID "An identifier for
  the Card Verification Value". The order is a click-and-collect order paid by card ("bring the card
  used for the order"). Card payment in a web shop is authorised by the payment provider; the order
  document that the shop keeps needs at most a masked number, as 21-PurchaseReceipt.xml shows
  (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`).
  Card industry rules forbid keeping the verification value after authorisation (PCI DSS, from own
  knowledge), so a stored order carrying it is implausible. This is the only CV2ID in the examples
  (`grep -rc CV2ID` over `*.xml`).
- Condition: the order carries no card verification value, and the card number only in masked form,
  unless the story gives the order a role in the card authorisation.
- Options: mask the PAN and drop CV2ID (preferred); the element can stay uncovered or be covered in a
  document whose purpose is the authorisation itself.
- Needs decision: yes

### retail/22#F3 · Low · The consumer's bank account in an order paid by card
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`
- Why: the order is paid by credit card; the buyer's current account (with bank and branch address)
  is used for nothing in it (IND5/IND6).
- Condition: no consumer bank account unless it is used.
- Options: drop it.
- Needs decision: no

### retail/22#F4 · Low · Requested collection from Monday, while the note says ready from Tuesday
- XPath: `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-01`
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- Why: RequestedDeliveryPeriod is "The period requested for delivery". It starts on Monday 2026-06-01;
  the note (written from the shop's side, in the buyer's order) says the set is ready from Tuesday
  2026-06-02. The order requests a collection on a day the goods are said not to be ready.
- Condition: the requested period and the readiness stated in the note agree.
- Options: start the period on 2026-06-02 (preferred), or drop "from Tuesday" from the note.
- Needs decision: no

## Checked and consistent
- BuyerCustomerParty and DeliveryParty are the consumer Robin Ashdale, SellerSupplierParty
  Brightmarket, as in 21-PurchaseReceipt.xml.
- The item `BM-551004` with GTIN `9523710000012`, brand Brackenmere, model Marrow, is the store's own
  garden set ordered from Brackenmere in `furniture/10-Order.xml`; HS 940169 and CPC 38112 fit a wooden
  frame.
- 899.00 + 6.5 % (58.44) = 957.44.
- The collection point (GLN `9522610900026`, garden department) differs from the goods-in GLN of
  08-Order.xml, as a sales floor should.
- check: the card number passes the Luhn check.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID`: an Incoterm (EXW) in a consumer order — refuted because EXW at
  the store states exactly that the buyer collects; Incoterms may be used for domestic sales.
- `/Order/cbc:ID`: an order number `RA-PO-…` "assigned by the sender", a consumer — refuted because a
  web shop numbers the orders it sends on the buyer's behalf, and the prefix is the buyer's initials.
