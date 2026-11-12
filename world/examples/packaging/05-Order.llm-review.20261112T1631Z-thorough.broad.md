# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/05-Order.xml`, Git blob `5869f45d431110e527ca796d40b56bf3f3390192` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### packaging/05#F1 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/05#F2 · Low · Shirts ordered for the garden department
- XPath: `/Order/cbc:AccountingCostCode` = `6120`
- XPath: `/Order/cbc:AccountingCost` = `Garden department`
- Why: AccountingCost is "The buyer's accounting cost centre, applied to the Order as a whole".
  Brightmarket books 600 men's shirts (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Cotton shirt`)
  to its garden department, while they are sold in the clothing department
  (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`).
  The same code and text are Brightmarket's cost centre for garden furniture in the furniture flow
  (`furniture/08-Order.xml:/Order/cbc:AccountingCost` = `Garden department`), so the value looks
  copied from the party.
- Condition: the cost centre is one shirts for the clothing department plausibly go to, or absent.
- Options: (a) a clothing department cost centre in order and invoice (preferred); (b) omit.
- Needs decision: no

### packaging/05#F3 · Low · Contacts do not fit their roles
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- Why: The buyer's "Buying office" carries the job title and department of a sales customer-service
  desk; the seller's contact is the mill's "Purchasing" desk, which does not handle sales orders
  (and also has a sales job title and department). Over all examples ('Buying office', 'Customer
  service officer', 'Sales') occurs in 41 contacts and ('Purchasing', …) in 52 (lxml count over
  `*.xml`).
- Condition: the buyer's contact is a buying function and the seller's a sales function, each with
  agreeing name, job title and department.
- Options: (a) give the mill a sales contact for its sales documents and Brightmarket a buyer job
  title/department (preferred); (b) neutral job titles.
- Needs decision: no

### packaging/05#F4 · Low · Retail marketing data in an order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Logo, online shop and social media profile address Brightmarket's customers; a purchase order
  to its supplier does nothing with them (IND5). On the receipts to shoppers (08, 09) they have a
  reason.
- Condition: the order carries none of them, or states a use.
- Options: (a) remove them from the order (preferred).
- Needs decision: no

### packaging/05#F5 · Low · No requested delivery date
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: The order says where (DDP, goods-in) but not when the spring shirts are wanted (IND6);
  `06-DespatchAdvice.xml` does not supply a date either.
- Condition: a requested delivery date or period is stated.
- Options: (a) Delivery/RequestedDeliveryPeriod (preferred).
- Needs decision: no

### packaging/05#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/05#F7 · Low · Default-looking registration date
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: 25 companies in all three countries carry 1 January 1996 (271 occurrences in 181 files,
  counted over `*.xml`); it reads as a default (IND5).
- Condition: the date is the mill's own, or absent.
- Options: (a) a date from the company history (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- 600 EA × 14.5 = 8700.00 = line = LineExtension = Payable; tax E/RESALE fits a retailer buying for
  resale; both parties in Coastal State.
- Item IDs: buyer's `BM-778120` and seller's `LT-SH-01` recur consistently in 06, 07 and the
  receipts (as seller's and manufacturer's IDs there).
- GLN `9522610900002` passes check_ids.py (GS1 prefix 952, reserved for examples).
- HS 620520 and CPC 28232 fit men's woven cotton shirts.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `DDP` for a delivery within Lumeport — refuted: DDP is valid
  for domestic sales and means the seller bears all costs to the buyer's door.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Lumeport` (also a town name) —
  refuted: a brand named after the town is plausible.
