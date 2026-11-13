# LLM review: 08-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/08-Order.xml`, Git blob `01257b4f8b6e604e5ea78070a814e95bca35ab3d` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/08#F1 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/08#F2 · Low · Own-line item carries the maker's brand
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/08#F3 · Low · Quotation line referenced twice and quoted price repeated as original price
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568`
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- Why: The order line points to quotation line 1 twice: through the dedicated `QuotationLineReference` and again through the line item's generic `LineReference` to `BF-DOC-26-0568`. `PricingReference/OriginalItemLocationQuantity` ("An original set of location-specific properties (e.g., price and quantity)") repeats the price 610 that `Price` already carries; nothing differs from an original. Neither adds information the order uses (IND5).
- Condition: Each relation of the order line is stated once, and `PricingReference` is present only where it carries a price or quantity that differs from or adds to `Price`.
- Options: (a, preferred) keep `QuotationLineReference` (with the header `QuotationDocumentReference`) and remove the `LineReference` and the `PricingReference`; (b) keep `PricingReference` only if a different list price is meant.
- Needs decision: no

### furniture/08#F4 · Low · Delivery place described only in text, though identified by GLN in the request
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: The request names the delivery place, the store's goods-in, with its GLN. The order, the document that actually fixes the delivery, describes the same place only by text in the delivery terms, and its `Delivery` has a delivery party but no location or requested date. A location identified elsewhere should carry the same identifier.
- Condition: The order's delivery location for the store's goods-in carries the GLN `9522610900019` used in 01.
- Options: (a, preferred) `Delivery/DeliveryLocation` with ID `9522610900019` and its name, as in 01; (b) at least the GLN on the delivery-terms location.
- Needs decision: no

### furniture/08#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- Sub-lines: 20 benches × 380 = 7 600 and 40 chairs × 115 = 4 600, together 12 200 = 20 sets × 610 = line extension and anticipated total; 40 chairs = two per set, as the description says.
- Tax: category E, rate 0, exemption RESALE for a retailer buying for resale, tax total 0.00 on taxable 12 200.
- Quantity bounds: minimum 10, maximum 20 SET, back order allowed between 5 and 10 SET; 10 = 20 − 10, consistent.
- `/Order/cac:QuotationDocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; the order (2026-03-16) is within its validity, price and quantity agree.

## Considered and refuted
- `/Order/cbc:AccountingCostCode` and `/Order/cac:OrderLine/cac:LineItem/cbc:AccountingCostCode`: duplicated — refuted, header and line cost codes are both defined and may coincide.
