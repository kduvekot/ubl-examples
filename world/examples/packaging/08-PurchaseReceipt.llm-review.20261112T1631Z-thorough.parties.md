# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

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

### packaging/08#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID, not a locale. The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/08#F2 · Low · The retailer's contact on a till receipt is its buying office
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- Why: Party/Contact is "The primary contact for this party"; on a receipt given to a consumer it is whom the customer contacts about the purchase (returns, complaints). Brightmarket's buying office deals with its suppliers (it is the buyer's contact in `05-Order.xml`), and its job title and department (customer service, sales) contradict its name. PointOfSaleContact is "The contact person at the point of sale where this purchase took place", but its telephone number is the buying office's (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 2511 0411`), not a number of the store or the clothing floor.
- Condition: the supplier's contact and the point-of-sale contact of the receipt are customer-facing contacts of the store, and differ from the buying office.
- Options: (a) preferred: a customer service contact for the store (Party/Contact) and the store's or floor's own number in PointOfSaleContact; (b) leave out the Party/Contact and keep only the point-of-sale contact.
- Needs decision: no

### packaging/08#F3 · Low · A cash customer's home address and bank account on the receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` = `Gull Lane`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: Person/FinancialAccount is "The financial account associated with this person". Robin Ashdale pays 70.00 in cash and gets change (`/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `10`), so no account is involved in the purchase, and nothing in the receipt (no delivery, no account sale, no loyalty scheme) needs the customer's residential address. A till receipt for a cash sale normally names no customer at all. The data looks copied from the person's master data.
- Condition: every customer detail on the receipt has a role in this purchase, or the receipt states the reason (for example a named receipt asked for by the customer).
- Options: (a) preferred: remove the bank account; keep the name and address only with a stated reason (e.g. a receipt made out for an expense claim), otherwise leave out the customer party; (b) change the story so that the customer pays from that account (card or transfer).
- Needs decision: no

### packaging/08#F4 · Low · The GTIN of the manufacturer's branded shirt is under the retailer's GS1 prefix
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a standard system"; under GS1 rules a GTIN is allocated by the brand owner from its own GS1 company prefix (own knowledge of the GS1 General Specifications). The GTIN `9522610000016` begins with the same seven digits `9522610` as the GLN of Brightmarket Stores (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`), so it reads as allocated by the retailer, while the item is a `Lumeport`-brand shirt made by Lumeport Textile Mill (`/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`), which identifies its items with its own numbers and the world item scheme in `05-Order.xml`, `06-DespatchAdvice.xml` and `07-Invoice.xml` (no GTIN there). Whether this is a problem depends on the length of Brightmarket's company prefix (with an eight-digit prefix `95226109` the GTIN would not be Brightmarket's) and on who owns the brand `Lumeport`, which the documents do not say. The GTIN occurs only in the two purchase receipts (Grep over `*.xml`).
- Condition: the GTIN is allocated by the brand owner of the shirt (the manufacturer, or Brightmarket if `Lumeport` is its private label), and the documents make that owner recognisable.
- Options: (a) preferred: decide who owns the brand; if Lumeport Textile Mill, give it a GS1 prefix and the GTIN in the order chain as well, or use no GTIN; (b) if `Lumeport` is Brightmarket's private label, keep the GTIN and make the brand ownership visible (e.g. Brightmarket as brand owner in the item).
- Needs decision: yes

## Checked and consistent
- Brightmarket Stores: the supplier block is identical in `09-PurchaseReceipt.xml` and matches the buyer block of `05-Order.xml` (IDs, tax ID `CO-1231233`, legal entity, address); trading name and the store's consumer-facing data (logo, web shop, social media profile) fit a receipt handed to a consumer.
- The item is the shirt Brightmarket bought in `05-Order.xml`: its seller's item number `BM-778120` is the buyer's item number there, the manufacturer's number `LT-SH-01` is the mill's seller's number there, and the world item ID `772030000090` is the standard item ID there; the manufacturer party has the mill's register ID `20412603`.
- check_ids.py: GLN `9522610900002`, GTIN `9522610000016` and the customer's account `XB64BLUM38010007251840` have valid check digits; the 952 prefix is GS1's range for examples.
- Robin Ashdale's address is in Lumeport (Coastal State), a residential address with a Lumeport register ID; the account is at the Bank of Lumeport main branch `380100`, which is also in the account number.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`: master data in a receipt — refuted because receipts are printed with the store's logo, web shop and social media details.
- `/PurchaseReceipt/cac:CashierContact/cbc:Name` = `Joss`: only a first name — refuted because a till receipt identifies the cashier by first name.
- `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`: the company name as a location name — refuted because the store is named after the company and the town; the description names the floor.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`: checked for the shared default date — refuted, Brightmarket has its own date.
