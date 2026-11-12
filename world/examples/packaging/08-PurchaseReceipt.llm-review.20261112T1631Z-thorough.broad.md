# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/08#F1 · Medium · Language code in LocaleCode
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/08#F2 · Low · Bank account of a customer who pays cash
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `10`
- Why: The shopper pays in cash (code 10, 70.00 tendered, 11.55 change); the receipt does nothing
  with Robin Ashdale's current account at the Bank of Lumeport. A shop has no business reason to
  print a cash customer's bank account on a receipt (IND5).
- Condition: the receipt carries no financial account of the customer, or the story gives it a use
  (e.g. a refund to that account).
- Options: (a) remove it (preferred).
- Needs decision: no

### packaging/08#F3 · Low · Shop contacts on a till receipt are the buying office
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- Why: For a shopper the seller's contact is customer service (questions, returns); Brightmarket gives
  its buying office, whose job is purchasing from suppliers (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`),
  with a sales job title. The point-of-sale contact ("The contact person at the point of sale")
  gives the buying office's number
  (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 2511 0411`),
  not the clothing floor or the store.
- Condition: the supplier's and point-of-sale contacts are functions a shopper can reach about this
  purchase, with agreeing name, job title and department.
- Options: (a) a store customer-service contact and the store's or floor's number (preferred);
  (b) drop PointOfSaleContact if the store has no number of its own.
- Needs decision: no

### packaging/08#F4 · Low · GTIN under the retailer's company prefix for a manufacturer-branded shirt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- Why: The GTIN uses the company prefix 9522610 of Brightmarket's own GLN
  (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`),
  but the shirt is made and branded by Lumeport Textile Mill (ManufacturerParty, brand "Lumeport").
  Under the GS1 General Specifications the brand owner allocates the GTIN; a retailer numbering
  goods for its own use takes restricted-circulation numbers (own knowledge). The mill's own documents
  carry no GTIN (`05-Order.xml`, `06-DespatchAdvice.xml`, `07-Invoice.xml`), so it is unclear whether
  the brand is meant to be Brightmarket's private label.
- Condition: either the GTIN is allocated by the brand owner, or the story makes Brightmarket the
  brand owner (private label), or the store's own number is a restricted-circulation number or an
  internal ID.
- Options: (a) decide who owns the brand and allocate accordingly (preferred); (b) keep the store's
  number only as SellersItemIdentification.
- Needs decision: yes

### packaging/08#F5 · Low · World item number is a valid UPC-A in the GS1 US range
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `772030000090`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 2 × 29.95 = 59.90 (BaseAmount); − 5.00 discount = 54.90 = line = LineExtension =
  TaxExclusive = TaxableAmount; 6.5 % × 54.90 = 3.5685 → 3.57; TaxInclusive 58.47; rounding −0.02 →
  58.45 payable (cash rounding to 0.05); 70.00 − 11.55 = 58.45 = PaidAmount.
- TaxInclusivePriceAmount 31.9 = 29.95 × 1.065 = 31.897; the description says sales tax is added at
  the till, matching the tax-exclusive PriceAmount.
- Item IDs: `BM-778120` (seller) and `LT-SH-01` (manufacturer) match the buyer's and seller's IDs in
  `05-Order.xml`; manufacturer party = the mill (`20412603`).
- Sold 2026-05-22, after the delivery of 2026-05-12 (`06-DespatchAdvice.xml`).
- GLN and GTIN pass check_ids.py (prefix 952, reserved for examples); customer account passes.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024` and
  the online shop and social media profile — refuted: a till receipt to a shopper normally shows the
  shop's logo, web shop and social media.
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
  with residential address on a cash receipt — refuted: a named receipt (e.g. for returns or a
  loyalty account) is plausible.
- `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount` = `-0.02` — refuted: cash
  rounding; the UBL definition ("added to produce the line extension amount") is UBL's own wording.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`
  ("Discount") for "5.00 off the pair" — refuted: fits.
