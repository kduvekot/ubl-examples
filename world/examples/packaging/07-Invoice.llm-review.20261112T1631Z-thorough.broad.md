# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/07-Invoice.xml`, Git blob `0345a2bca9a5957f58f15a04460ca368ab893cee` (committed)
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

### packaging/07#F1 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/07#F2 · Low · Invoice does not reference the delivery it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525`
- Why: The goods were announced in `06-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `LTM-DA-26-0526`
  the same day, but the invoice carries neither a DespatchDocumentReference nor a Delivery with a
  date, so the link between the delivery and its invoice exists only through the order number, and
  the date of supply is not stated (IND6). No example refers to the despatch advice (grep over
  `*.xml` for `LTM-DA-26-0526`).
- Condition: the invoice references the despatch advice and/or states the actual delivery date.
- Options: (a) DespatchDocumentReference to `LTM-DA-26-0526` (preferred: the document exists in the
  flow); (b) Delivery/ActualDeliveryDate.
- Needs decision: no

### packaging/07#F3 · Low · Shirts invoiced to the garden department
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole, expressed
  as text". Men's shirts sold in the clothing department
  (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`)
  are booked to the garden department, Brightmarket's cost centre for garden furniture
  (`furniture/08-Order.xml:/Order/cbc:AccountingCost` = `Garden department`); taken over from
  `05-Order.xml:/Order/cbc:AccountingCost` = `Garden department`.
- Condition: the cost centre fits a clothing purchase (and agrees with the order), or is absent.
- Options: (a) a clothing department cost centre (preferred); (b) omit.
- Needs decision: no

### packaging/07#F4 · Low · Contacts do not fit invoicing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- Why: The supplier's contact on its invoice is its purchasing desk (named Purchasing, but in Sales);
  the accounting customer's contact is the buying office, not accounts payable. Neither handles the
  payment this invoice requests.
- Condition: each accounting party's contact handles the invoice, with agreeing name, job title and
  department.
- Options: (a) accounts receivable / payable contacts (preferred); (b) a sales contact for the mill.
- Needs decision: no

### packaging/07#F5 · Low · Retail marketing data in an invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The customer's logo, online shop and social media play no part in billing it (IND5).
- Condition: the invoice carries none of them, or states a use.
- Options: (a) remove them (preferred).
- Needs decision: no

### packaging/07#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/07#F7 · Low · Default-looking registration date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: 25 companies in all three countries carry 1 January 1996 (271 occurrences in 181 files,
  counted over `*.xml`); it reads as a default (IND5).
- Condition: the date is the mill's own, or absent.
- Options: (a) a date from the company history (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- Order reference resolves to `05-Order.xml`; 600 EA × 14.5 = 8700.00, tax E/RESALE, parties and item
  agree with the order and with `06-DespatchAdvice.xml` (600 delivered).
- Due 2026-05-12 + 30 days = 2026-06-11 (three places); penalty 1.5 % × 8700.00 = 130.50; penalty
  period from 2026-06-12.
- Payee account `XB35BLUM38020504608076` (Lumeport Textile Mill Ltd, branch 380205) passes
  check_ids.py; RF18LTMINV260529 passes.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LT-SH-01`: the buyer's
  item ID `BM-778120` from the order is missing — refuted: optional, and the seller's ID identifies
  the item unambiguously.
