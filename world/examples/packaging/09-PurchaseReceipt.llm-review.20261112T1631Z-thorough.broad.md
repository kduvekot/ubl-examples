# LLM review: 09-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/09#F1 · Medium · Language code in LocaleCode
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/09#F2 · Low · Contacts do not fit a retail sale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The shop's contact on a till receipt is its buying office (purchasing from suppliers), and the
  point-of-sale contact repeats that office's number instead of the store's or the clothing floor's.
  The customer's contact is named "Purchasing" but has the job title and department of a sales
  customer-service desk.
- Condition: the shop's and point-of-sale contacts are reachable by a shopper about this purchase;
  the customer's contact has agreeing name, job title and department.
- Options: (a) a store customer-service contact and a purchasing job title/department for Velumi
  (preferred); (b) drop PointOfSaleContact if the store has no number of its own.
- Needs decision: no

### packaging/09#F3 · Low · GTIN under the retailer's company prefix for a manufacturer-branded shirt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- Why: The GTIN uses Brightmarket's company prefix 9522610 (its GLN
  `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`),
  while the shirt is made and branded by Lumeport Textile Mill. Under GS1 rules the brand owner
  allocates the GTIN (own knowledge); the mill's documents carry no GTIN. Same as in
  `08-PurchaseReceipt.xml`.
- Condition: either the brand owner allocates the GTIN, or the story makes Brightmarket the brand
  owner, or the store's number is a restricted-circulation or internal number.
- Options: (a) decide who owns the brand and allocate accordingly (preferred); (b) keep the store's
  number as SellersItemIdentification only.
- Needs decision: yes

### packaging/09#F4 · Low · World item number is a valid UPC-A in the GS1 US range
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `772030000090`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/09#F5 · Low · Default-looking registration date
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: 25 companies in all three countries carry 1 January 1996 (271 occurrences in 181 files,
  counted over `*.xml`); it reads as a default (IND5).
- Condition: the date is Velumi's own, or absent.
- Options: (a) a date from the company history (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- Prices: 29.95 XBL (as in `08-PurchaseReceipt.xml`) × 0.4 = 11.98 XLC; 3 × 11.98 = 35.940;
  6.5 % × 35.940 = 2.3361 → 2.336; total 38.276 = PayableAmount = PaidAmount.
- Tax in Lume: 35.940 × 2.5 = 89.85 = 3 × 29.95; 6.5 % × 89.85 = 5.840 → 5.84; 2.336 × 2.5 = 5.84.
  TaxExchangeRate (XLC → XBL, × 2.5) and PricingExchangeRate (XBL → XLC, × 0.4) are inverses, same date.
- PurchaseReceipt has no TaxCurrencyCode in the model; the second TaxTotal in XBL and the tax
  exchange rate state the tax currency.
- The note on paying in coral agrees with DocumentCurrencyCode XLC and the card payment (code 54).
- Masked PAN, card network and issuer are consistent; the cardholder is the customer.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
  tagged `en-XB` for a Lisavan address — refuted: the English rendering carries the issuer's locale
  (Brightmarket, Bayvarra), as elsewhere in the flow.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024` and the
  web shop / social media — refuted: plausible on a receipt to a customer.
- A wholesaler (`/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649`)
  paying standard sales tax on three shirts — refuted: a retail purchase (e.g. samples) is taxable;
  no resale exemption is claimed.
- `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `38.276` with three decimals — refuted: Coral has 3
  fractional digits in the world's currency list (`world/codelists/CurrencyCode-2.4-world.gc`).
