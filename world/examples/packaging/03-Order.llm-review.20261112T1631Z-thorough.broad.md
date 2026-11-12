# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/03-Order.xml`, Git blob `4c3acea07de9e59031f62d8970fa32ff7a492ca6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/03#F1 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/03#F2 · Low · Cost centre "Raw cotton" for garment bags
- XPath: `/Order/cbc:AccountingCostCode` = `2200`
- XPath: `/Order/cbc:AccountingCost` = `Raw cotton`
- Why: AccountingCost is "The buyer's accounting cost centre, applied to the Order as a whole".
  The mill books polyethylene garment bags (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Garment bag`)
  to its raw-cotton account. The same code and text are the mill's account for its cotton purchases
  in the cotton flow (`cotton/08-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`), so the
  value looks copied from the party, not chosen for this purchase.
- Condition: the cost centre named for this order is one a packaging purchase plausibly goes to, or
  the element is absent.
- Options: (a) a packaging-materials or consumables cost centre (preferred); (b) omit both elements.
- Needs decision: no

### packaging/03#F3 · Low · Buyer's contact: name, job title and department disagree
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is named "Purchasing" (with a purchasing mailbox), which fits the buyer, but its
  job title and department are those of a sales customer-service desk. The triple ('Purchasing',
  'Customer service officer', 'Sales') occurs in 52 contacts over all examples (lxml count over
  `*.xml`).
- Condition: name, job title and department of the buyer's contact describe the same buying function.
- Options: (a) a purchasing/procurement job title and department (preferred); (b) neutral values.
- Needs decision: no

### packaging/03#F4 · Low · Seller's bank account in an order
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: An order involves no payment; the account is given again where it is used, in
  `04-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
  Copied master data (IND5).
- Condition: the order carries no financial account, or states why.
- Options: (a) remove it (preferred).
- Needs decision: no

### packaging/03#F5 · Low · No requested delivery date
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Textile Mill, goods-in`
- Why: The order (DAP, delivery to the mill) says where but not when the 20 000 bags are wanted; the
  mill needs them before it bags the shirts ordered on 2026-05-07 in `05-Order.xml`. Nothing may be
  implied from absence (IND6).
- Condition: the order states a requested delivery date or period, or the story says why not.
- Options: (a) Delivery/RequestedDeliveryPeriod (preferred).
- Needs decision: no

### packaging/03#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: 12 digits with a correct GS1 check digit (computed: 0), i.e. a GTIN-12 with GS1 US prefix 077,
  a range assigned to real companies (own knowledge). All world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/03#F7 · Low · Default-looking registration date
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Both parties, and 25 companies in all three countries, carry 1 January 1996 (271 occurrences in
  181 files, counted over `*.xml`); it reads as a default (IND5).
- Condition: each date is the company's own, or absent.
- Options: (a) dates from the company histories (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- 20 000 EA × 0.08 = 1600.00 = line = LineExtension = Payable; 20 000 bags = 40 boxes of 500.
- Tax E with RESALE "Sale for resale or manufacture": the bags become part of the packaged shirts the
  mill sells (`05-Order.xml`, item "in a garment bag"); domestic Coastal State sale.
- Item, quantity, price and tax agree with `04-Invoice.xml`.
- HS 392321 and CPC 36410 fit polyethylene bags.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `1312`: a weaving mill
  selling finished shirts (in `05-Order.xml`) — refuted: IndustryClassificationCode states the
  party's (main) activity and may repeat; a mill that also makes up garments is plausible.
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`: delivery
  party equal to the buyer — refuted: it identifies who receives at the DAP place; harmless.
