# LLM review: 09-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

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

### packaging/09#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID, not a locale. The same value occurs 362 times in 213 examples (Grep over `*.xml`); the Lisavan customer of this receipt has none.
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/09#F2 · Low · The contacts do not fit: the retailer's buying office, and a "Purchasing" contact in sales for the customer
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party". On a receipt Brightmarket's contact should be customer-facing, but it is its buying office, and the point-of-sale contact ("The contact person at the point of sale where this purchase took place") has the buying office's number. Velumi Trading's contact is named purchasing (fitting a business that buys) but has a sales job title and department; the combination occurs in 52 contacts across the examples (lxml count over `*.xml`).
- Condition: Brightmarket's contacts on the receipt are customer-facing contacts of the store; Velumi's contact has a name, job title and department that agree.
- Options: (a) preferred: as in `08-PurchaseReceipt.xml`, a store contact and number; a purchasing job title and department for Velumi; (b) omit the Party/Contact elements on the receipt.
- Needs decision: no

### packaging/09#F3 · Low · Velumi's address is tagged en-XB here, en-XL in its own documents
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: the English renderings of Velumi Trading's Lisavan address carry `languageID="en-XB"` here, but `en-XL` where Velumi issues the document (`sea/05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`, languageID `en-XL`). Velumi's English address is tagged en-XB in 11 examples and en-XL in 8 (lxml count over `*.xml`); the tag follows the issuer's country, so the same text of the same address is attributed to two varieties of English.
- Condition: the same text of Velumi's address carries the same languageID in every example, or the convention is stated.
- Options: (a) preferred: tag a party's English names with the variety of the party's country (en-XL), as in Velumi's own documents; (b) adopt the issuer's variety as an explicit convention.
- Needs decision: yes

### packaging/09#F4 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". Velumi Trading (Island companies register) shares this date with 24 companies in the registers of Bayvarra and Urvania (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: Velumi's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: an individual date; (b) remove; (c) confirm as a story fact.
- Needs decision: yes

### packaging/09#F5 · Low · The GTIN of the manufacturer's branded shirt is under the retailer's GS1 prefix
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a standard system"; under GS1 rules a GTIN is allocated by the brand owner from its own GS1 company prefix (own knowledge of the GS1 General Specifications). The GTIN `9522610000016` begins with the same seven digits `9522610` as the GLN of Brightmarket Stores (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`), so it reads as allocated by the retailer, while the item is a `Lumeport`-brand shirt made by Lumeport Textile Mill (`/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`), which identifies its items with its own numbers and the world item scheme in `05-Order.xml`, `06-DespatchAdvice.xml` and `07-Invoice.xml` (no GTIN there). Whether this is a problem depends on the length of Brightmarket's company prefix (with an eight-digit prefix `95226109` the GTIN would not be Brightmarket's) and on who owns the brand `Lumeport`, which the documents do not say. The GTIN occurs only in the two purchase receipts (Grep over `*.xml`).
- Condition: the GTIN is allocated by the brand owner of the shirt, and the documents make that owner recognisable (the same as in `08-PurchaseReceipt.xml`).
- Options: (a) preferred: decide who owns the brand and allocate or drop the GTIN accordingly; (b) if `Lumeport` is Brightmarket's private label, keep the GTIN and make the brand ownership visible.
- Needs decision: yes

### packaging/09#F6 · Low · A customs trader ID on a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: the customs trader identifier identifies Velumi to customs; the receipt is a sale over the counter in Lumeport with Coastal State sales tax charged, not an export sale, so customs has no role in it. It looks copied from master data.
- Condition: the receipt carries the customs ID only if the sale involves customs (e.g. a tax-free export sale).
- Options: (a) preferred: leave it out; (b) if the shirts are meant to be exported by Velumi, show that in the tax treatment.
- Needs decision: no

## Checked and consistent
- Brightmarket's supplier block is identical to the one in `08-PurchaseReceipt.xml` (compared line by line); item identifiers and manufacturer party agree with `05-Order.xml` and `08-PurchaseReceipt.xml`.
- Velumi Trading: register ID `IC41859` in PartyIdentification, CompanyID and endpoint `XL:IC41859`; Island limited company, small, active, in the Island companies register; Lisavan address with a delivery-point ID, in Lisavan and English.
- Card holder name `VELUMI TRADING` is the customer; the card issuer `BSELXLSL` is a world bank identifier, and owner code `BSEL` is not in `world/codelists/sources/bic/owner-codes.txt`.
- check_ids.py: GLN `9522610900002` and GTIN `9522610000016` valid.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649`: a household-goods wholesaler buying three shirts at retail — refuted because a company may buy goods for its own use (e.g. staff clothing) at a store and pay with its company card.
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `40351721`: a delivery-point ID instead of a postal zone — refuted because it is Lisavu's own address register (schemeID `urn:ubl-examples:world:XL:delivery-point`), the national level the agreed rules prescribe for address registers.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`: master data in a receipt — refuted because receipts carry the store's web and social media details for the customer.
