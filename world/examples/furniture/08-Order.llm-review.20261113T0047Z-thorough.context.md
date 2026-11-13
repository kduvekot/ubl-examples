# LLM review: 08-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/08#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/08#F2 · Low · Line item UUID that nothing uses
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:UUID` = `4278e92c-6141-5575-b08f-555e19cf4b75`
- Why: `LineItem/UUID` is "A universally unique identifier for this line item". It is useful when another document refers to the line item by it; no example refers to this UUID (Grep for `4278e92c` over `world/examples/*/*.xml` finds only this file), and the repeat order `10-Order.xml` has no line item UUID. The line is already identified by its `ID` and the order number. Without a use it is a filler (IND5).
- Condition: the line item UUID is absent, or a document of the flow refers to it.
- Options: (a) remove it (preferred); (b) let the invoice or credit note refer to the line by it.
- Needs decision: no

### furniture/08#F3 · Low · "Original" price identical to the price, next to a note that says so
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.`
- Why: `PricingReference/OriginalItemLocationQuantity` is "An original set of location-specific properties (e.g., price and quantity) associated with this item"; it says something when the price ordered differs from an original one. Here the original price equals the price, and the note and the quotation line reference already say the price is the quoted one. The aggregate adds no information.
- Condition: `OriginalItemLocationQuantity` is absent, or its price differs from the line price for a reason the story gives.
- Options: (a) remove the pricing reference (preferred); (b) keep it only in an order whose price departs from the quotation.
- Needs decision: no

### furniture/08#F4 · Low · Quotation line referenced twice
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568`
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- Why: The order line has the dedicated `QuotationLineReference` ("A reference to a quotation line associated with this order line"), and the line item additionally has a generic `LineReference` to line 1 of the same quotation. The two references say the same thing; the generic one is meant for lines of documents for which no dedicated reference exists.
- Condition: the quotation line is referenced once, by `QuotationLineReference` (with its document, if needed, through `/Order/cac:QuotationDocumentReference`).
- Options: (a) remove the `LineItem/LineReference` (preferred); (b) none other seen.
- Needs decision: no

### furniture/08#F5 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`), and the store even has its own item number for it (`BM-551004`). `BrandName` = the maker's name contradicts the note and the item description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the texts.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/08#F6 · Low · Buyer's master data copied into the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in an order for garden sets (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `MinimumQuantity` 10, `MaximumQuantity` 20 with `Quantity` 20, `BackOrderAllowedIndicator` true with backorder 5 to 10 sets: a coherent instruction (deliver at least 10, back-order the rest in lots of 5 to 10).
- Sub line items: 20 benches × 380 = 7600 and 40 chairs × 115 = 4600, sum 12200 = line amount = 20 sets × 610; two chairs per set as the note says.
- `WarrantyParty` = the maker with a two-year `WarrantyValidityPeriod`: fits a maker's warranty.
- `AccountingCostCode`/`AccountingCost` "Garden department" is the buyer's own cost centre, as defined.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:ItemPriceExtension/cbc:Amount` = `12200.00`: equal to the line extension amount — refuted as a filler because the two have different definitions (price × quantity versus amount including allowances) and happen to coincide without allowances.
- `/Order/cac:OrderLine/cac:LineItem/cbc:InspectionMethodCode` = `VISUAL`: suspected without purpose — refuted because goods-in inspection of furniture is a real requirement of the buyer.
